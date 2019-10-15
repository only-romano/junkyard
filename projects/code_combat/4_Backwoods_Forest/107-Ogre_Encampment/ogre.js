// If there is an enemy, attack it.
// Otherwise, attack the chest!

while(true) {
    // Use if/else.
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        hero.attack(enemy);
    } else {
        hero.attack("Chest");
    }
}
