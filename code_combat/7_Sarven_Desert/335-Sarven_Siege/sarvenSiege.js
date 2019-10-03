// Defend your towers in this replayable challenge level!
// Step on an X if you have 20 gold to build a soldier.

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
