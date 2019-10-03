hero.enemyInRange = function (enemy) {
    // Return true if the enemy is less than 5 units away.
    return hero.distanceTo(enemy) < 5;
}

hero.cleaveOrAttack = function (enemy) {
    if (hero.isReady("cleave")) {
        hero.cleave(enemy);
    } 
    else {
        hero.attack(enemy);
    }
}

while(true) {
    var enemy = hero.findNearestEnemy();
    if(enemy) {
        // Check the distance of the enemy by calling enemyInRange.
        if (hero.enemyInRange(enemy)) {
            hero.cleaveOrAttack(enemy);
        }
    }
}
