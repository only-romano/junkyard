// Survive both waves by shielding and cleaving.
// When "cleave" is not ready, use your shield skill.
// You'll need at least 142 health to survive.
while(true) {
    var enemy = hero.findNearestEnemy();
    if (hero.isReady("cleave")) {
        hero.cleave(enemy);
    } else if (hero.isReady("warcry")) {
        hero.warcry();
    } else {
        hero.shield();
    }
}
