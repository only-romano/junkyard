// Cleave the munchkins to survive!
// Make sure you have enough armor.
while(true) {
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        if (hero.isReady("cleave")) {
            hero.cleave(enemy);
        }
        else {
            hero.attack(enemy);
        }
    }
}
