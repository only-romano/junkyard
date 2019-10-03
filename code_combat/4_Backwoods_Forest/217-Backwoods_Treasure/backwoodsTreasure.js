// Collect 100 gold from two or three groves.
// If you win, it gets harder (and more rewarding).
// If you lose, you must wait a day before you can resubmit.
// Remember, each submission gets a new random seed.


function onSpawn() {
    while (true) {
        pet.moveXY(51, 8);
        pet.moveXY(72, 12);
        pet.moveXY(65, 24);
        pet.moveXY(hero.pos.x, hero.pos.y);
        pet.moveXY(70, 46);
        pet.moveXY(48, 59);
        pet.moveXY(hero.pos.x, hero.pos.y);
        pet.moveXY(14, 20);
        pet.moveXY(12, 67);
        pet.moveXY(26, 65);
        pet.moveXY(hero.pos.x, hero.pos.y);
    }
}

pet.on("spawn", onSpawn);

while (true) {

    var flag = hero.findFlag();
    if (flag) {
        if (hero.isReady("jump"))
            hero.jumpTo(flag.pos);
        else hero.move(flag.pos);
        if (flag.color == "black" && hero.canCast("invisibility"))
            hero.cast("invisibility", hero);
        hero.pickUpFlag(flag);
    }

    if (hero.canCast("summon-burl")) hero.cast("summon-burl");
    if (hero.canCast("summon-undead")) hero.cast("summon-undead");
    if (hero.canCast("raise-dead")) hero.cast("raise-dead");

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
        
        if (hero.health < hero.maxHealth / 2) {
            var friend = hero.findNearest(hero.findFriends());
            if (friend && friend.type != "burl" && hero.canCast("drain-life") && hero.distanceTo(friend) <= 15)
                hero.cast("drain-life", friend);
        }
}
