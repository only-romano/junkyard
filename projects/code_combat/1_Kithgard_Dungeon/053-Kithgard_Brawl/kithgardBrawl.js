// 7 level
// Used items: Unholy Tome V, Vine Stuff, Emperor's gloves, Precious ring

function onSpawn() {
    while (true) {
        var item = pet.findNearestByType("potion");
        if (item) {
            pet.fetch(item);
        }
    }
}

pet.on("spawn", onSpawn);

while (true) {

    var flag = hero.findFlag();
    if (flag) {
        if (flag.color == "green") {
            if (hero.canCast("invisibility"))
                hero.cast("invisibility");
        }
        hero.jumpTo(flag.pos);
        hero.pickUpFlag(flag);
    }

    if (hero.canCast("summon-burl")) hero.cast("summon-burl");
    if (hero.canCast("summon-undead")) hero.cast("summon-undead");
    if (hero.canCast("raise-dead")) hero.cast("raise-dead");

     var enemy = hero.findNearestEnemy();
    if (enemy && !hero.hasEffect("hide")) {
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
