// Take down those ogres!

while(true) {
    if (hero.isReady("warcry")) {
        hero.warcry();
    }
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        if (hero.isReady("cleave")) {
            hero.cleave(enemy);
        } else {
            hero.attack(enemy);
        }
    }

}
