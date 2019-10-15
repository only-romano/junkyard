while(true) {
    var enemy = hero.findNearestEnemy();
    var distance = hero.distanceTo(enemy);
    if (distance < 20) {
        // Attack if they get too close to the peasant.
        hero.attack(enemy);
    }
    // Else, stay close to the peasant! Use else.
    else {
        hero.moveXY(40, 37);
    }
}
