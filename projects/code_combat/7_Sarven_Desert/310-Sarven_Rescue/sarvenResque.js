// Rescue the peasant from the bandits and return her to the village.
// Choose the path that suits you, avoiding patrols or facing them head on.
// Potions will grant random effects–some good, some bad.
// Feeling brave? Bonus if you can loot the ogre treasure chest.
function attackIt() {
    while (true) {
        var flag = hero.findFlag();
        if (flag) {
            if (flag.color == "green") {
                break;
            }
            if (hero.isReady("jump"))
                hero.jumpTo(flag.pos);
            hero.pickUpFlag(flag);
        }
    
        var enemy = hero.findNearestEnemy();
        if (enemy && enemy.type != "sand-yak")
            if (hero.distanceTo(enemy) < 10) hero.attack(enemy);
    }
}

while (true) {
    var flag = hero.findFlag();
    if (flag) {
        if (flag.color == "black") {
            hero.pickUpFlag(flag);
            attackIt();
        } else {
            hero.pickUpFlag(flag);
        }
    }
}
