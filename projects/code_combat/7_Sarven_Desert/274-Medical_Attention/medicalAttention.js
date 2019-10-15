// Ask the healer for help when you're under one-half health.

while (true) {
    var currentHealth = hero.health;
    var healingThreshold = hero.maxHealth / 2;
    // If your current health is less than the threshold,
    // move to the healing point and say, "heal me".
    // Otherwise, attack. You'll need to fight hard!
    if (currentHealth < healingThreshold) {
        hero.moveXY(65, 46);
    }

    var enemy = hero.findNearestEnemy();
    if (enemy)
        hero.attack(enemy);
}
