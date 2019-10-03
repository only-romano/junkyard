// Only build if you see an enemy.

// The function defines THREE parameters.
function maybeBuildSomething(typeToBuild, x, y) {
    hero.moveXY(x, y);
    // Find the nearest enemy.
    var enemy = hero.findNearestEnemy();
    // If there is an enemy
    if (enemy) {
        // then use buildXY with typeToBuild, x, and y
        // Use the variable typeToBuild as a first argument.
        hero.buildXY(typeToBuild, x, y);
    }
}

// You don't need to change the code below.
while(true) {
    // Call maybeBuildSomething with "fire-trap" and the coordinates of the bottom X.
    maybeBuildSomething("fire-trap", 40, 20);
    // Call maybeBuildSomething, with "fence" at the left X!
    maybeBuildSomething("fence", 26, 34);
    // Call maybeBuildSomething with "fire-trap" at the top X!
    maybeBuildSomething("fire-trap", 40, 50);
    // Call maybeBuildSomething with "fence" at the right X!
    maybeBuildSomething("fence", 54, 34);
}
