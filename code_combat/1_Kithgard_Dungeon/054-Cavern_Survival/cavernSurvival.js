// Stay alive longer than the enemy hero!
while(true) {
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        var distance = hero.distanceTo(enemy);

        if (distance <= 30) {
            if (hero.canCast("chain-lightning"))
                hero.cast("chain-lightning", enemy);
            else if (distance > 15 && hero.canCast("poison-cloud"))
                hero.cast("poison-cloud", enemy);
            else if (hero.canCast("raise-dead"))
                hero.cast("raise-dead");
            else if (distance <= 25 && hero.canCast("fear"))
                hero.cast("fear", enemy);
            else if (hero.canCast("summon-undead"))
                hero.cast("summon-undead");
            else if (distance <= 15 && hero.canCast("drain-life"))
                hero.cast("drain-life", enemy);
            else
                hero.attack(enemy);
        } else {
            if (hero.canCast("summon-burl"))
                hero.cast("summon-burl");
            else if (hero.canCast("summon-undead"))
                hero.cast("summon-undead");
            else if (hero.canCast("raise-dead"))
                hero.cast("raise-dead");
            else if (distance <= 45)
                hero.attack(enemy);
        }
    } else {
        if (hero.canCast("summon-burl"))
            hero.cast("summon-burl");
        else if (hero.canCast("summon-undead"))
            hero.cast("summon-undead");
        else if (hero.canCast("raise-dead"))
            hero.cast("raise-dead");
    }

    var item = hero.findNearestItem();
    if (item && item.type != "poison") {
        pet.fetch(item);
    }
    
    if (hero.health < hero.maxHealth) {
        var friend = hero.findFriends();
        if (friend.length && friend[0] && hero.canCast("drain-life") && hero.distanceTo(friend[0]) <= 15) {
            hero.cast("drain-life", friend[0]);
        }
    }
}
