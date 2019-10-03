// Stay alive for one minute.
// If you win, it gets harder (and more rewarding).
// If you lose, you must wait a day before you can resubmit.
// Remember, each submission gets a new random seed.

function onSpawn() {
    while (true) {
        var item = hero.findNearestItem();
        if (item) {
            pet.fetch(item);
        }
    }
}


pet.on("spawn", onSpawn);


while (true) {

    var flag = hero.findFlag();
    if (flag) {
        if (hero.isReady("jump"))
            hero.jumpTo(flag.pos);
        hero.pickUpFlag(flag);
    }

    if (hero.canCast("summon-burl")) hero.cast("summon-burl");
    if (hero.canCast("summon-undead")) hero.cast("summon-undead");

    var enemy = hero.findNearestEnemy();
    if (enemy) {
        var distance = hero.distanceTo(enemy);
        if (distance < 25 && hero.canCast("fear"))
            hero.cast("fear", enemy);
        else if (distance < 30 && hero.canCast("chain-lightning")) hero.cast("chain-lightning", enemy);
        else if (distance < 30 && hero.canCast("poison-cloud")) hero.cast("poison-cloud", enemy);
        else if (distance < 15 && hero.canCast("drain-life"))
            hero.cast("drain-life", enemy);
        else hero.attack(enemy);
    }

    if (hero.canCast("raise-dead")) hero.cast("raise-dead");
}
