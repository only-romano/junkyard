// Step 4 of creating a Pac-Man style arcade game.

// The game layout and items. Scroll down.
game.spawnXY("forest", 16, 16);
game.spawnXY("forest", 32, 16);
game.spawnXY("forest", 48, 16);
game.spawnXY("forest", 64, 16);
game.spawnXY("forest", 16, 32);
game.spawnXY("forest", 32, 32);
game.spawnXY("forest", 48, 32);
game.spawnXY("forest", 64, 32);
game.spawnXY("forest", 16, 48);
game.spawnXY("forest", 32, 48);
game.spawnXY("forest", 48, 48);
game.spawnXY("forest", 64, 48);

game.spawnXY("bronze-coin", 16, 8);
game.spawnXY("bronze-coin", 24, 8);
game.spawnXY("bronze-coin", 32, 8);
game.spawnXY("bronze-coin", 48, 8);
game.spawnXY("bronze-coin", 56, 8);
game.spawnXY("bronze-coin", 64, 8);
game.spawnXY("bronze-coin", 72, 8);

game.spawnXY("bronze-coin", 8, 16);
game.spawnXY("bronze-coin", 24, 16);
game.spawnXY("bronze-coin", 40, 16);
game.spawnXY("bronze-coin", 56, 16);
game.spawnXY("bronze-coin", 72, 16);

game.spawnXY("bronze-coin", 8, 24);
game.spawnXY("bronze-coin", 16, 24);
game.spawnXY("bronze-coin", 24, 24);
game.spawnXY("bronze-coin", 32, 24);
game.spawnXY("bronze-coin", 40, 24);
game.spawnXY("bronze-coin", 48, 24);
game.spawnXY("bronze-coin", 56, 24);
game.spawnXY("bronze-coin", 64, 24);
game.spawnXY("bronze-coin", 72, 24);

game.spawnXY("bronze-coin", 24, 32);
game.spawnXY("bronze-coin", 56, 32);

game.spawnXY("bronze-coin", 8, 40);
game.spawnXY("bronze-coin", 16, 40);
game.spawnXY("bronze-coin", 24, 40);
game.spawnXY("bronze-coin", 32, 40);
game.spawnXY("bronze-coin", 40, 40);
game.spawnXY("bronze-coin", 48, 40);
game.spawnXY("bronze-coin", 56, 40);
game.spawnXY("bronze-coin", 64, 40);
game.spawnXY("bronze-coin", 72, 40);

game.spawnXY("bronze-coin", 8, 48);
game.spawnXY("bronze-coin", 24, 48);
game.spawnXY("bronze-coin", 40, 48);
game.spawnXY("bronze-coin", 56, 48);
game.spawnXY("bronze-coin", 72, 48);

game.spawnXY("bronze-coin", 8, 56);
game.spawnXY("bronze-coin", 16, 56);
game.spawnXY("bronze-coin", 24, 56);
game.spawnXY("bronze-coin", 32, 56);
game.spawnXY("bronze-coin", 48, 56);
game.spawnXY("bronze-coin", 56, 56);
game.spawnXY("bronze-coin", 64, 56);
game.spawnXY("bronze-coin", 72, 56);

game.spawnXY("mushroom", 40, 8);
game.spawnXY("mushroom", 8, 32);
game.spawnXY("mushroom", 72, 32);
game.spawnXY("mushroom", 40, 56);

game.score = 1000;
// The duration of power-ups.
game.powerDuration = 6;
// The time until a power-up runs out. Used for UI.
game.powerTime = 0;
// The time a power-up expires. Used internally.
game.powerEndTime = 0;
ui.track(game, "time");
ui.track(game, "score");
// Adding ui for game.powerTime:
ui.track(game, "powerTime");

game.addCollectGoal();
game.addSurviveGoal();

var player = game.spawnPlayerXY("knight", 8, 8);
player.maxSpeed = 30;

// The function make the player big and strong.
function powerPlayerUp() {
    player.scale = 2;
    player.attackDamage = 100;
    game.powerEndTime = game.time + game.powerDuration;
}

// The function return the player in the normal state.
function powerPlayerDown() {
    player.scale = 1;
    player.attackDamage = 1;
}

function onCollect(event) {
    var player = event.target;
    var item = event.other;
    if (item.type == "bronze-coin") {
        game.score += 1;
    }
    if (item.type == "mushroom") {
        game.score += 5;
        // Use powerPlayerUp to strengthen the player:
        powerPlayerUp();
    }
}

function onCollide(event) {
    var player = event.target;
    var other = event.other;
    // If other is a "scout" and the player's scale is 2:
    if (other.type == "scout" && player.scale == 2) {
        // Defeat the other with the defeat method:
        other.defeat();
    }
}


player.on("collect", onCollect);
// Assign the event handler for the player's "collide" event:
player.on("collide", onCollide);

var generator = game.spawnXY("generator", 41, 31);
generator.spawnType = "scout";
generator.spawnDelay = 6;

function onSpawn(event) {
    var unit = event.target;
    unit.maxSpeed = 8;
    unit.attackDamage = player.maxHealth;
    while (true) {
        // Enemies run away from the big player.
        if (player.scale == 2) {
            unit.behavior = "RunsAway";
        }
        else {
            unit.behavior = "AttacksNearest";
        }
    }
}

function onDefeat(event) {
    // Increase game.score for defeated enemies:
    game.score += 10;
}

game.setActionFor("scout", "spawn", onSpawn);
game.setActionFor("scout", "defeat", onDefeat);


function checkTimeScore() {
    game.score -= 0.5;
    if (game.score < 0) {
        game.score = 0;
    }
}

function checkPowerTimer() {
    // Remaining power time.
    game.powerTime = game.powerEndTime - game.time;
    if (game.powerTime <= 0) {
        game.powerTime = 0;
        // If the player is powered, then it's time to power-down.
        if (player.scale == 2) {
            powerPlayerDown();
        }
    }
}

// Lets combine all the time based functions.
function checkTimers() {
    checkTimeScore();
    checkPowerTimer();
}

while (true) {
    checkTimers();
}

// Win the game.
