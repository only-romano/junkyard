// Remember that enemies may not yet exist.
while (true) {
    var enemy = hero.findNearestEnemy();
    // If there is an enemy, attack it!
    if (enemy) {
        hero.attack(enemy);
    }
}
