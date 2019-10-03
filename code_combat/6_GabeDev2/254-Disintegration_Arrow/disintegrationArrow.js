// Destroy at least 50 defeated ogres.

// This spawns and configures an archer.
function spawnArcher(x, y) {
    var archer = game.spawnXY("archer", x, y);
    archer.behavior = "Defends";
    archer.attackDamage = 20;
}

// This spawns and configures an ogre.
function spawnMunchkin(x, y) {
    var ogre = game.spawnXY("munchkin", x, y);
    ogre.behavior = "AttacksNearest";
}

// Spawns some archers in a row.
function spawnArcherWall() {
    spawnArcher(30, 12);
    spawnArcher(30, 23);
    spawnArcher(30, 34);
    spawnArcher(30, 45);
    spawnArcher(30, 56);
}

// Spawns an ogre wave with a random offset for variety.
function spawnOgreWave() {
    var offset = game.randomInteger(-6, 6);
    spawnMunchkin(80, 16 + offset);
    spawnMunchkin(80, 22 + offset);
    spawnMunchkin(80, 28 + offset);
    spawnMunchkin(80, 34 + offset);
    spawnMunchkin(80, 40 + offset);
    spawnMunchkin(80, 46 + offset);
    spawnMunchkin(80, 52 + offset);
}

function onDefeat(event) {
    var unit = event.target;
    // Increase the game.defeated counter by 1.
    game.defeated++;
    // Use unit.destroy() to destroy it.
    unit.destroy();
}

// Set "munchkin"s "defeat" event handlers to onDefeat.
game.setActionFor("munchkin", "defeat", onDefeat);

game.defeated = 0;
game.spawnTime = 0;
// Add a manual goal.
var goal = game.addManualGoal("Defeat 77 ogres.");
ui.track(game, "defeated");

function checkSpawnTimer() {
    if (game.time > game.spawnTime) {
        spawnOgreWave();
        game.spawnTime += 1;
    }
}

function checkGoal() {
    // If the game.defeated counter is greater than 77:
    if (game.defeated > 77) {
        // Set the goal as successfully completed.
        game.setGoalState(goal, true);
    }
}

spawnArcherWall();
while (true) {
    checkSpawnTimer();
    checkGoal();
}
