// Learn the difference between destroy and defeat.

// Spawn the enemies.
var ogre1 = game.spawnXY("ogre", 12, 18);
ogre1.behavior = "AttacksNearest";
var ogre2 = game.spawnXY("ogre", 68, 50);
ogre2.behavior = "AttacksNearest";

var munchkinGenerator = game.spawnXY("generator", 12, 50);
munchkinGenerator.spawnAI = "Scampers";
munchkinGenerator.spawnType = "munchkin";

var scoutGenerator = game.spawnXY("generator", 68, 12);
scoutGenerator.spawnAI = "Scampers";
scoutGenerator.spawnType = "scout";

// The fences which we will destroy later.
var leftFence = game.spawnXY("fence", 26, 14);
var rightFence = game.spawnXY("fence", 54 , 50);

var player = game.spawnPlayerXY("knight", 40, 34);
player.maxSpeed = 16;
player.attackDamage = 20;

// The global game counters.
game.scoutsSpawned = 0;
game.munchkinsSpawned = 0;
game.bossesDefeated = 0;
ui.track(game, "scoutsSpawned");
ui.track(game, "munchkinsSpawned");
ui.track(game, "bossesDefeated");

var bossesGoal = game.addManualGoal("Defeat 2 big ogres.");

function onSpawn(event) {
    var unit = event.target;
    if (unit.type == "scout") {
        game.scoutsSpawned += 1;
    }
    if (game.scoutsSpawned >= 3) {
        // Defeat scoutGenerator with the defeat() method.
        scoutGenerator.defeat();
        // Destroy rightFence with the destroy() method.
        rightFence.destroy();
    }
    if (unit.type == "munchkin") {
        game.munchkinsSpawned += 1;
    }
    if (game.munchkinsSpawned >= 2) {
        // Defeat munchkinGenerator.
        munchkinGenerator.defeat();
        // Destroy the leftFence.
        leftFence.destroy();
    }
}

function onDefeat(event) {
    var unit = event.target;
    if (unit.type == "ogre") {
        // Increase the game.bossesDefeated counter by 1:
        game.bossesDefeated += 1;
    }
}

game.setActionFor("munchkin", "spawn", onSpawn);
game.setActionFor("scout", "spawn", onSpawn);
game.setActionFor("ogre", "defeat", onDefeat);

while (true) {
    if (game.bossesDefeated >= 2) {
        game.setGoalState(bossesGoal, true);
    }
}
