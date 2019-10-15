// The smaller ogres here do more damage!
// Attack the ogres with the least health first.
while(true) {
    var weakest = null;
    var leastHealth = 99999;
    var enemyIndex = 0;
    var enemies = hero.findEnemies();

    // Loop through all enemies.
    while (enemyIndex < enemies.length) {
        // If an enemy's health is less than leastHealth,
        var enemy = enemies[enemyIndex];
        if (enemy.health < leastHealth) {
            // make it the weakest and set leastHealth to its health.
            weakest = enemy;
            leastHealth = enemy.health;
        }
        //  Don't forget to increase enemyIndex by 1.
        enemyIndex++;
    }
    if (weakest) {
        if (hero.canCast("chain-lightning"))
            hero.cast("chain-lightning", weakest);  // Fix for tiny weak heroes
        // Attack the weakest ogre.
        hero.attack(weakest);
    }
}
