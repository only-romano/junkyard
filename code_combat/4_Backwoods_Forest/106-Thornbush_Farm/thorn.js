// Patrol the village entrances.
// Build a "fire-trap" when you see an ogre.
// Don't blow up any peasants!

while(true) {
    hero.moveXY(43, 50);
    var top = hero.findNearestEnemy();
    if (top) {
        hero.buildXY("fire-trap", 43, 50);
    }

    hero.moveXY(25, 34);
    var left = hero.findNearestEnemy();
    // Check if `left` exists.
    if (left) {
        // Build a trap at 25, 34 if the enemy exists.
        hero.buildXY("fire-trap", 25, 34);
    }

    hero.moveXY(43, 20);
    // Set a variable for the bottom enemy.
    var bottom = hero.findNearestEnemy();
    // Check if the bottom enemy exists.
    if (bottom) {
        // Build a trap at 43, 20 if an enemy exists.
        hero.buildXY("fire-trap", 43, 20);
    }
}
