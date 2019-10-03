while(true) {
    var enemy = hero.findNearestEnemy();
    if(enemy) {
        // Find the distance to the enemy with distanceTo.
        var distance = hero.distanceTo(enemy);
        // If the distance is less than 5 meters...
        if (distance < 5) {
            // ... if "cleave" is ready, cleave!
            if (hero.isReady("cleave")) {
                hero.cleave(enemy);
            }
            // ... else, just attack.
            else {
                hero.attack(enemy);
            }
        }
            
    }
}
