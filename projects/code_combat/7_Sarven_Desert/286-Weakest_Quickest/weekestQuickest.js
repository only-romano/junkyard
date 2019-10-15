// Defeat shamans to survive.

// This function finds the weakest enemy.
function findWeakestEnemy() {
    var enemies = hero.findEnemies();
    var weakest = null;
    var leastHealth = 99999;
    var enemyIndex = 0;
    // Loop through enemies:
    while (enemyIndex < enemies.length) {
        var enemy = enemies[enemyIndex];
        // If an enemy's health is less than leastHealth:
        if (enemy.health < leastHealth) {
            // Make it the leastHealth 
            weakest = enemy;
            // and set leastHealth to its health.
            leastHealth = enemy.health;
        }
        enemyIndex++;
    }
    return weakest;
}

while(true) {
    // Find the weakest enemy with the function:
    var weakestShaman = findWeakestEnemy();
    // If the weakest enemy exists:
    if (weakestShaman) {
        // Attack it!
        hero.attack(weakestShaman);
    }
}
