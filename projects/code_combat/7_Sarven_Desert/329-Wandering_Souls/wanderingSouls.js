// Defeat skeletons and collect lightstones.

while (true) {
    var enemies = hero.findEnemies();
    var enemyIndex = 0;
    while (enemyIndex < enemies.length) {
        var enemy = enemies[enemyIndex];
        // Attack while enemy has health.
        while (enemy.health > 0) {
            hero.attack(enemy);
        }
        enemyIndex += 1;
    }
    var items = hero.findItems();
    var itemIndex = 0;
    // Iterate over all items.
    while (itemIndex < items.length) {
        var item = items[itemIndex];
        // While the distance greater than 2:
        while (hero.distanceTo(item) > 2)
            // Try to take the item.
            hero.moveXY(item.pos.x, item.pos.y);
        // Don't forget to increase itemIndex.
        itemIndex += 1;
    }
}
