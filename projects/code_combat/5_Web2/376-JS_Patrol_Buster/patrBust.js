// Remember that enemies may not yet exist.
while (true) {
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        // If there is an enemy, attack it!
        hero.attack(enemy);
    }
}
