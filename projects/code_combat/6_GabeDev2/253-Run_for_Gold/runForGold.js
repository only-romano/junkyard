// Generate randomly placed treasures and destroy them later.

// This spawns an item with lifetime at a random point.
function spawnValuable(itemType, lifetime) {
    var x = game.randomInteger(12, 68);
    var y = game.randomInteger(12, 56);
    var item = game.spawnXY(itemType, x, y);
    item.destroyTime = game.time + lifetime;
}

// This spawns the treasure set.
function spawnTreasures() {
    spawnValuable("bronze-coin", 6);
    spawnValuable("silver-coin", 5);
    spawnValuable("gold-coin", 4);
    spawnValuable("gem", 2);
}

// The event handler for items.
function onSpawn(event) {
    var item = event.target;
    while(true) {
        // If game time is greater than item destroyTime: ;
        if (item.destroyTime < game.time) {
            // Call item's destroy() method:
            item.destroy();
        }
    }
}

game.setActionFor("bronze-coin", "spawn", onSpawn);
game.setActionFor("silver-coin", "spawn", onSpawn);
game.setActionFor("gold-coin", "spawn", onSpawn);
game.setActionFor("gem", "spawn", onSpawn);

// Game settings, goals and UI.
game.spawnTime = 0;
game.spawnInterval = 3;
game.score = 0;
if (!db.get("topScore")) {
    db.set("topScore", 0);
}
ui.track(game, "time");
ui.track(game, "score");
ui.track(db, "topScore");
var goal = game.addManualGoal("Collect at least 50 gold in 30 seconds.");

// The player setup.
var player = game.spawnPlayerXY("captain", 40, 34);
player.maxSpeed = 25;

function onCollect(event) {
    var item = event.other;
    // If the item has a "value" property:
    if (item.value) {
        // Increase the game score by item's value:
        game.score += item.value;
    }
}

player.on("collect", onCollect);

// This checks timers for treasure spawning.
function checkSpawns() {
    // If game.time is greater than game.spawnTime:
    if (game.time > game.spawnTime) {
        // Call spawnTreasures to create more items.
        spawnTreasures();
        // Increase game.spawnTime by game.spawnInterval:
        game.spawnTime += game.spawnInterval;
    }
}

// This checks the goal state.
function checkGoal() {
    if (game.score > 50) {
        game.setGoalState(goal, true);
    }
    else {
        game.setGoalState(goal, false);
    }
}

// This checks the game state.
function checkGameOver() {
    if (game.time > 30) {
        checkGoal();
        db.set("topScore", game.score);
    }
}

while (true) {
    checkSpawns();
    checkGameOver();
}
