// This function attacks the nearest enemy.
function findAndAttackEnemy() {
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        hero.attack(enemy);
    }
}

// Define a function to cleave enemies (but only when the ability is ready).
function findAndCleaveEnemy() {
    // Find the nearest enemy:
    var enemy = hero.findNearestEnemy();
    // If an enemy exists:
    if (enemy) {
        // And if "cleave" is ready:
        if (hero.isReady("cleave")) {
            // It's time to cleave!
            hero.cleave(enemy);
        }
    }
}

// In your main loop, patrol, cleave, and attack.
while (true) {
    // Move to the patrol point, cleave, and attack.
    hero.moveXY(35, 34);
    findAndCleaveEnemy();
    findAndAttackEnemy();
    
    // Move to the other point:
    hero.moveXY(60, 31);
    // Use findAndCleaveEnemy function:
    findAndCleaveEnemy();
    
    // Use findAndAttackEnemy function:
    findAndAttackEnemy();
    
}
