/*
This level is intended to be for advanced players.

The solution should be pretty complex with a lot of moving parts.
It might also be a bit of a gear check unless you use creative methods.

You need to make your way to the first trial (Oasis of Marr) defeating
enemies along the way.
When you reach it, pick all the mushrooms to trigger the trial to begin.
If you survive the onslaught, make your way to the next Oasis for the
second trial, then the Temple.
When all trials are complete you will have to face the final boss.

Good luck!

HINT: Glasses with a high visual range help tremendously on this level
so buy the best you can get.

HINT: the unit 'type' for the oasis guardians is 'oasis-guardian'
*/

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
                else if (distance < 45) hero.attack(enemy);
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
