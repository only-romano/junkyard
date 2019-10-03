// The "defeat" event signals that a unit was defeated.
game.spawnPlayerXY("captain", 40, 35);
game.addSurviveGoal();
game.addCollectGoal(8);

function onSpawn(event) {
    while(true) {
        var unit = event.target;
        var enemy = unit.findNearestEnemy();
        if(enemy) {
            unit.attack(enemy);
        }
    }
}

// When a unit is defeated, spawn a gold coin.
function onDefeat(event) {
    var unit = event.target;
    // Set x to unit.pos.x, plus a random number between -5 and 5
    var x = unit.pos.x + game.randomInteger(-5, 5);
    // Set y to unit.pos.y, plus a random number between -5 and 5
    var y = unit.pos.y + game.randomInteger(-5, 5);
    // Spawn a "gold-coin" at x, y
    game.spawnXY("gold-coin", x, y);
}

game.setActionFor("munchkin", "spawn", onSpawn);
game.setActionFor("munchkin", "defeat", onDefeat);

var spawnTime = 0;
while(true) {
    if(game.time > spawnTime) {
        var x = game.randomInteger(10, 70);
        var y = game.randomInteger(10, 60);
        game.spawnXY("munchkin", x, y);
        spawnTime = game.time + game.randomInteger(1,4);
    }
}
