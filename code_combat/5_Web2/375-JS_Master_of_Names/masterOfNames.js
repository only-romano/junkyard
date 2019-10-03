// Your hero doesn't know the names of these enemies!
// Use the findNearestEnemy method on your new glasses.

// Assign the result of hero.findNearestEnemy() to the variable enemy1:
while(true) {
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        hero.attack(enemy);
    }
}
