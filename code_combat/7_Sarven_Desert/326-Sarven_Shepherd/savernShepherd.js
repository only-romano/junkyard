// Use while loops to pick out the ogre

while(true) {
    var enemies = hero.findEnemies();
    var enemyIndex = 0;

    // Wrap this logic in a while loop to attack all enemies.
    // Find the array's length with:  enemies.length
    while (enemyIndex < enemies.length) {
        var enemy = enemies[enemyIndex];
        // "!=" means "not equal to."
        if (enemy.type != "sand-yak") {
        // While the enemy's health is greater than 0, attack it!
            while (enemy.health > 0) {
                if (hero.isReady("bash")) hero.bash(enemy);
                else hero.attack(enemy);
            }
        }
        enemyIndex++;
    }
    // Between waves, move back to the center.
    hero.moveXY(40, 32);
}
