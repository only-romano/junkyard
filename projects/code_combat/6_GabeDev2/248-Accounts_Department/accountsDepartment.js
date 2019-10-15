// Count collected item values and use them for scoring.

// Setup characters.
var player = game.spawnPlayerXY("captain", 40, 34);
player.maxSpeed = 20;

// Chests of gems are the most valuable items.
game.spawnXY("chest", 68, 56);
game.spawnXY("chest", 14, 14);

// This function spawns a random item in a random place.
function spawnRandomItem() {
    var itemNumber = game.randomInteger(1, 3);
    var x = game.randomInteger(12, 68);
    var y = game.randomInteger(12, 56);
    if (itemNumber == 1) {
        game.spawnXY("bronze-coin", x, y);
    }
    else if (itemNumber == 2) {
        game.spawnXY("gold-coin", x, y);
    }
    else if (itemNumber == 3) {
        game.spawnXY("gem", x, y);
    }
}

var itemInterval = 1;
var itemSpawnTime = 0;
function checkSpawnTimer() {
    if (game.time >= itemSpawnTime) {
        // Call the spawnRandomItem function.
        spawnRandomItem();
        itemSpawnTime += itemInterval;
    }
}

game.score = 0;

// The "collect" event is triggered by collecting something.
function onCollect(event) {
    // event.target contains the collector.
    var collector = event.target;
    // event.other contains the collected item.
    var item = event.other;
    if (item.value) {
        // Adding health power for valuable items.
        collector.health += item.value;
        // Increase the game score by the item's `value`:
        game.score += item.value;
    }
}

// Assigning onCollect handler for "player" on "collect" event.
player.on("collect", onCollect);

// The score the player needs to win.
var requiredScore = 220;
var goldGoal = game.addManualGoal('Collect at least 220 gold in 20 seconds.');
ui.track(game, "score");

function checkGoals() {
    if (game.score >= requiredScore) {
        game.setGoalState(goldGoal, true);
    }
}

while(true) {
    checkSpawnTimer();
    checkGoals();
}
