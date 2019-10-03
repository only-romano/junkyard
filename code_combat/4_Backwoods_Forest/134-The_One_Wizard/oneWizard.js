// Defeat as many ogres as you can.
// Use 'cast' and 'canCast' for spells.

while(true) {
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        var distance = hero.distanceTo(enemy);
        if (distance <= 30) {
            if (hero.canCast("chain-lightning")) {
                hero.cast("chain-lightning", enemy);
            } else {
                if (enemy.type === "ogre") {
                    hero.moveXY(7, 42);
                } else {
                    hero.attack(enemy);
                }
            }
        } else {
            if (hero.canCast("lightning-bolt")) {
                hero.cast("lightning-bolt", enemy);
            }
            else if (hero.canCast("regen")) {
                hero.cast("regen", hero);
            }
        }
    }
}
