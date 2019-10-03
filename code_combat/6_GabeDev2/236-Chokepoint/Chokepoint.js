// Ogres are advancing through the forest lanes!
// Spawn some soldiers and have them defend their lanes!

function defendLane(event) {
    // Remember to create a variable for the target, to remember:
    var unit = event.target;
    // Save the unit's starting pos.x
    var startX = unit.pos.x;
    while(true) {
        var enemy = unit.findNearestEnemy();
        // If there is an enemy.
        if (enemy) {
            // Use unit.attack to attack the enemy:
            unit.attack(enemy);
        }
        else {
            // Move the unit back to it's starting x and y.
            unit.moveXY(startX, 16);
        }
        
    }
}

game.spawnXY("soldier", 9, 16);
game.spawnXY("soldier", 30, 16);
game.spawnXY("soldier", 54, 16);
game.spawnXY("soldier", 75, 16);

// Set the event handler defendLane on "spawn" event for "soldier"s.
game.setActionFor("soldier", "spawn", defendLane);
