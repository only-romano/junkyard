// Learn to use X Marks as triggers!

// Set up the maze.
game.spawnMaze(3);
game.spawnXY("forest", 20, 45);
game.spawnXY("forest", 20, 28);
game.spawnXY("forest", 20, 58);
game.spawnXY("forest", 36, 60);
game.spawnXY("forest", 36, 44);
game.spawnXY("forest", 36, 13);

// Player and goal.
var player = game.spawnPlayerXY("knight", 60, 34);
var goal = game.addManualGoal("Defeat 30 munchkins!");

// Fire cannons!
var fire1 = game.spawnXY("fire-spewer", 27, 12);
var fire2 = game.spawnXY("fire-spewer", 29, 12);
var fire3 = game.spawnXY("fire-spewer", 11, 12);
var fire4 = game.spawnXY("fire-spewer", 13, 12);
fire1.direction = "vertical";
fire2.direction = "vertical";
fire3.direction = "vertical";
fire4.direction = "vertical";
fire1.spamCooldown = 0;
fire2.spamCooldown = 0;
fire3.spamCooldown = 0;
fire4.spamCooldown = 0;
// NOTE Setting disabled to true stops the fire.
fire1.disabled = true;
fire2.disabled = true;
fire3.disabled = true;
fire4.disabled = true;

// These are our triggers.
// boneX will trigger fire.
var boneX = game.spawnXY("x-mark-bones", 60, 50);
// stoneX will trigger munchkin spawns.
var stoneX = game.spawnXY("x-mark-stone", 60, 22);

game.spawns = 0;
game.defeated = 0;
ui.track(game, "spawns");
ui.track(game, "defeated");

// Count defeated munchkins.
function onDefeat(event) {
    game.defeated += 1;
}

game.setActionFor("munchkin", "defeat", onDefeat);

// Spawns 2 munchkins every 0.25 seconds.
game.spawnTime = 0;
game.spawnCooldown = 0.25;

function spawnMunchkinsOverTime() {
    if(game.time >= game.spawnTime) {
        var m1 = game.spawnXY("munchkin", 11, 57);
        var m2 = game.spawnXY("munchkin", 28, 57);
        m1.behavior = "Scampers";
        m2.behavior = "Scampers";
        // Count number of spawns.
        game.spawns += 2;
        game.spawnTime = game.time + game.spawnCooldown;
    }
}

// Turn on fire if the player is near boneX
function checkBoneX() {
    if(boneX.distanceTo(player) <= 1) {
        player.say("Firing!");
        fire1.disabled = false;
        // Set disabled to False for the other cannons
        fire2.disabled = false;
        fire3.disabled = false;
        fire4.disabled = false;
    } else {
        fire1.disabled = true;
        fire2.disabled = true;
        fire3.disabled = true;
        fire4.disabled = true;
    }
}

// Spawn munchkins if player is near stoneX
function checkStoneX() {
    // If the distance between stoneX and the player <= 1:
    if (player.distanceTo(stoneX) <= 1) {
        // Call the spawnMunchkinsOverTime() function
        spawnMunchkinsOverTime();
    }
}

function checkVictory() {
    if(game.defeated >= 30) {
        // Use game.setGoalState(goal, true)
        game.setGoalState(goal, true);
    }
}

// Main game loop.
while(true) {
    checkStoneX();
    checkBoneX();
    checkVictory();
}
