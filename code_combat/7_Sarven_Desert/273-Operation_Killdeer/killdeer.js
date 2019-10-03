// Lure the ogres into a trap. These ogres are careful.
// They will only follow if the hero is injured.

// This function checks the hero's health 
// and returns a Boolean value.
function shouldRun() {
    if (hero.health < hero.maxHealth / 2) {
        return true;
    } else {
        return false;
    }
}

while (true) {
    // Move to the X only if shouldRun() returns true
    if (shouldRun()) {
        hero.moveXY(75, 37);
    }
    // Else, attack!
    else {
        var enemy = hero.findNearestEnemy();
        if (enemy) {
            hero.attack(enemy);
        }
    }
}
