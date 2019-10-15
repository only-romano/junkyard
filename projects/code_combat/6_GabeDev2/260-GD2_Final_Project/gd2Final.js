// Create your own game!
// Spawn a player with spawnPlayerXY()
// Spawn objects into the game with spawnXY()
// Add at least one goal!

game.spawnMaze(1);
var chest = game.spawnXY("chest", 60, 59);
var mashroom = game.spawnXY("mushroom", 60, 10);

var generator = game.spawnXY("generator", 28, 60);
generator.spawnType = "thrower";

var spewer = game.spawnXY("fire-spewer", 43, 10);
spewer.direction = "horizontal";


// functions
function onSpawnPlayer() {
    player.say("He-he-he, here we are!");
    player.moveXY(13, 51);
    player.say("Let's find these treasures! They must be somewhere around.");
}

function onCollect(event) {
    var item = event.other.type;
    player.say(item);
    if (item == "mushroom") {
        player.maxHealth *= 2;
        player.health = player.maxHealth;
        player.attackDamage = 25;
    } else if (item == "gem") {
        runPhase2();
        game.addMoveGoalXY(12, 50);
        game.addSurviveGoal();
        game.setGoalState(goal, true);
    }
}

function runPhase2() {
    player.say("No way! I did it! I gotta get outta here!");
    spewer.direction = "vertical";
    game.spawnXY("generator", 10, 10);
    game.spawnXY("generator", 28, 60);
    var gen = game.spawnXY("generator", 10, 35);
    gen.spawnType = "thrower";
}

var player = game.spawnPlayerXY("captain", 12, 58);

// Event handlers
player.on("spawn", onSpawnPlayer);
player.on("collect", onCollect);

// Base settings
var goal = game.addManualGoal("Find the tresures!");
var goal2 = null;

