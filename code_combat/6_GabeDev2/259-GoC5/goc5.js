// Step 5 of creating a Pac-Man style arcade game.
// GAME PARAMETERS
// Game parameters define the game difficulty.

// Change the game parameters to balance the game.
// How long power-ups work (seconds).
var POWER_DURATION = 4; // ∆
// Score values for coins, mushrooms and ogres.
var COIN_SCORE = 1; // ∆
var MUSHROOM_SCORE = 5; // ∆
var DEFEATED_SCORE = 10; // ∆
// How much the score is reduced each game tick.
var TIME_SCORE = 1; // ∆
// The player and ogre speeds.
var HERO_SPEED = 20; // ∆
var OGRE_SPEED = 15; // ∆
// The ogre spawn delay (seconds).
var SPAWN_DELAY = 4; // ∆

// LEVEL LAYOUT
// Obstacles and collectable items.
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

// GAME SETUP
// Goals, UI and game global variables.
game.score = 1000;
game.powerDuration = POWER_DURATION;
game.powerTime = 0;
game.powerEndTime = 0;
ui.track(game, "time");
ui.track(game, "score");
ui.track(game, "powerTime");
game.addCollectGoal();
game.addSurviveGoal();

// HERO SETUP
// The player, its parameters and event handlers.
var player = game.spawnPlayerXY("knight", 8, 8);
player.maxSpeed = HERO_SPEED;

function powerPlayerUp() {
    player.scale = 2;
    player.attackDamage = 100;
    game.powerEndTime = game.time + game.powerDuration;
}

function powerPlayerDown() {
    player.scale = 1;
    player.attackDamage = 1;
}

function onCollect(event) {
    var player = event.target;
    var item = event.other;
    if (item.type == "bronze-coin") {
        game.score += COIN_SCORE;
    }
    if (item.type == "mushroom") {
        game.score += MUSHROOM_SCORE;
        powerPlayerUp();
    }
}

function onCollide(event) {
    var player = event.target;
    var other = event.other;
    if (other.type == "scout" && player.scale == 2) {
        other.defeat();
    }
}

player.on("collect", onCollect);
player.on("collide", onCollide);

// ENEMIES
// The enemy generator, enemies` events and parameters.
var generator = game.spawnXY("generator", 41, 31);
generator.spawnType = "scout";
generator.spawnDelay = SPAWN_DELAY;

function onSpawn(event) {
    var unit = event.target;
    unit.maxSpeed = OGRE_SPEED;
    unit.attackDamage = player.maxHealth;
    while (true) {
        if (player.scale == 2) {
            unit.behavior = "RunsAway";
        }
        else {
            unit.behavior = "AttacksNearest";
        }
    }
}

function onDefeat(event) {
    game.score += DEFEATED_SCORE;
}

game.setActionFor("scout", "spawn", onSpawn);
game.setActionFor("scout", "defeat", onDefeat);

// GAME LOOP
// The main game loop with time-based functions.
function checkTimeScore() {
    game.score -= TIME_SCORE;
    if (game.score < 0) {
        game.score = 0;
    }
}

function checkPowerTimer() {
    game.powerTime = game.powerEndTime - game.time;
    if (game.powerTime <= 0) {
        game.powerTime = 0;
        if (player.scale == 2) {
            powerPlayerDown();
        }
    }
}

function checkTimers() {
    checkTimeScore();
    checkPowerTimer();
}

while (true) {
    checkTimers();
}

// Win the game!
