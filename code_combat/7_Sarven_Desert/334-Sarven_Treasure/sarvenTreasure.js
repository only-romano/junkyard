// Collect 150 gold while evading ogres with teleporters.
// If you win, it gets harder (and more rewarding).
// If you lose, you must wait a day before you can resubmit.
// Remember, each submission gets a new random seed.

function onSpawn() {
    while (true) {
        pet.moveXY(16, 56);
        pet.moveXY(64, 56);
        pet.moveXY(64, 20);
        pet.moveXY(16, 20);
        pet.moveXY(hero.pos.x, hero.pos.y);
    }
}

function attackIt() {
    if (hero.canCast("summon-burl"))
        hero.cast('summon-burl');
    if (hero.canCast("summon-undead"))
        hero.cast('summon-undead');
    if (hero.canCast("raise-dead"))
        hero.cast('raise-dead');
        
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        var distance = hero.distanceTo(enemy);
        if (hero.health < 700 && distance < 15)
            hero.cast("drain-life", enemy);
        else if (hero.canCast("chain-lightning") && distance < 30)
            hero.cast("chain-lightning", enemy);
        else if (hero.canCast("poison-cloud") && distance < 30)
            hero.cast("poison-cloud", enemy);
    }
}

function collectIt() {
    var items = hero.findItems();
    var coolest = null;
    var rating = 0;
    for (var i = 0; i < items.length; i++) {
        var item = items[i];
        var distance = hero.distanceTo(item);
        if (item.value && item.value / distance > rating) {
            coolest = item;
            rating = item.value / distance;
        }
    }
    if (coolest) {
        if (hero.isReady("jump"))
            hero.jumpTo(coolest.pos);
        else
            hero.moveXY(coolest.pos.x, coolest.pos.y);
    }
}

pet.on("spawn", onSpawn);

while (true) {
    attackIt();
    collectIt();
}
