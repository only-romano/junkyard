// Your cleave is on a 10 second cooldown.
// Use an else-statement to defend yourself while recharging.

while(true) {
    var enemy = hero.findNearestEnemy();
    if(hero.isReady("cleave")) {
        hero.cleave();
    }
    // Write else: to do something when "cleave" isn't ready:
    else {
        // Be sure to attack the enemy:
        hero.attack(enemy);
    }
}
