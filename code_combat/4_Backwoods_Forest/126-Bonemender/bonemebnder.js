// Heal allied soldiers to survive the siege.
while(true) {
    if (hero.canCast("regen")) {
        var bernardDistance = hero.distanceTo("Bernard");
        if(bernardDistance < 10) {
            // "Bernard" needs regeneration!
            hero.cast("regen", "Bernard");
        }
        
        // Use "if" and "distanceTo" to regenerate "Chandra"
        // if she is closer than 10 meters away.
        var chandraDistance = hero.distanceTo("Chandra");
        if (chandraDistance < 10) {
            hero.cast("regen", "Chandra");
        }
        
    }
    else {
        // If you aren't casting "regen", use "if" and "distanceTo"
        // to attack enemies that are closer than hero.attackRang
        var enemy = hero.findNearestEnemy();
        if (enemy) {
            if (hero.distanceTo(enemy) <= hero.attackRange) {
                hero.attack(enemy);
            }
        }
    }
}
