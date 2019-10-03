// Check if the mines are safe for the workers.

function checkEnemyOrSafe(target) {
    // If `target` (the parameter) exists:
    if (target) {
        // Then attack target.
        hero.attack(target);
    }
    // Otherwise:
    else {
        // Use say() to call the peasants.
        hero.say("Here");
    }
}

while (true) {
    // Move to, and check the top right X mark.
    hero.moveXY(64, 54);
    var enemy1 = hero.findNearestEnemy();
    checkEnemyOrSafe(enemy1);
    
    // Move to the bottom left X mark.
    hero.moveXY(15, 14);
    // Save the result of findNearestEnemy() in a variable.
    var enemy2 = hero.findNearestEnemy();
    // Call checkEnemyOrSafe, and pass the
    // result of findNearestEnemy as the argument.
    checkEnemyOrSafe(enemy2);
}
