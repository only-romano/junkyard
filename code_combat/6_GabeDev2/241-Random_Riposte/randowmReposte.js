// Use game.randomInteger(min,max) to add randomness!
game.spawnPlayerXY("knight", 40, 35);
game.addSurviveGoal();
game.addDefeatGoal(8);

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

// Spawn an ogre every 0 to 4 seconds.
var spawnTime = 0;
while(true) {
    if(game.time > spawnTime) {
        // Spawn a "munchkin" at a random location
        // Set x to a random number between 10 and 70
        var x = game.randomInteger(10, 70);
        // Set y to a random number between 10 and 60
        var y = game.randomInteger(10, 60);
        // Spawn a "munchkin" at x, y
        game.spawnXY("munchkin", x, y);
        // Spawn again in 0 through 4 seconds
        spawnTime = game.time + game.randomInteger(0, 4);
    }
}
