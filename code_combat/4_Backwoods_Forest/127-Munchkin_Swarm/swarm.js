while(true) {
    // Check the distance to the nearest enemy.
    var nearestEnemy = hero.findNearestEnemy();
    var distance = hero.distanceTo(nearestEnemy);
    // If it comes closer than 10 meters, cleave it!
    if (distance < 10) {
        hero.cleave(nearestEnemy);
    }
    // Else, attack the "Chest" by name.
    else {
        hero.attack("Chest");
    }
    
}
