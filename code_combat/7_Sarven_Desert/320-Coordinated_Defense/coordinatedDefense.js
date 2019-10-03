// Protect the peasants from the ogres.

while (true) {
    // Get an array of enemies.
    var enemies = hero.findEnemies();
    // If the array is not empty.
    if (enemies.length > 0) {
        // Attack the first enemy from "enemies" array.
        hero.attack(enemies[0]);
        // Return to the start position.
        hero.moveXY(40, 20);
    }
}
