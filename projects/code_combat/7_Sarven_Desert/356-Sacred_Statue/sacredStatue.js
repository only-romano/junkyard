// Walk to a few points around the ogre camps, defeating any enemies along the way.
// Visit the statue to begin the event.
// Stand your ground and defeat the attacking ogres.

// Hint: fight close to the statue for it's assistance during the battle.

// After you defeat all of the waves, you will have to face off against the Ancient Cyclops!
function attackIt() {
    while (true) {
        var flag = hero.findFlag();
        if (flag) {
            if (flag.color == "green") {
                break;
            }
            hero.jumpTo(flag.pos);
            hero.pickUpFlag(flag);
        }
    
        if (hero.canCast("summon-burl")) hero.cast("summon-burl");
        if (hero.canCast("summon-undead")) hero.cast("summon-undead");
        if (hero.canCast("raise-dead")) hero.cast("raise-dead");
    
         var enemy = hero.findNearestEnemy();
        if (enemy && enemy.type != "sand-yak") {
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
