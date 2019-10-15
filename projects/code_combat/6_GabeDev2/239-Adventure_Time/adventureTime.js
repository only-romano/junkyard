// game.time is the time that has passed in the game
game.spawnPlayerXY("guardian", 10, 35);
game.addSurviveGoal();
game.addDefeatGoal(5);

function onSpawn(event) {
    while(true) {
        var unit = event.target;
        var enemy = unit.findNearestEnemy();
        if(enemy) {
            unit.attack(enemy);
        }
    }
}

game.setActionFor("munchkin", "spawn", onSpawn);

// game.time starts at zero, and counts upward in seconds
var spawnTime = 0;
while(true) {
    // spawnTime is the time we want to spawn at
    if(game.time > spawnTime) {
        // Spawn a "munchkin" at 60, 35
        game.spawnXY("munchkin", 60, 35);
        // Set spawnTime equal to game.time + 2
        // so an enemy will spawn every 2 seconds.
        spawnTime = game.time + 2;
    }
}
