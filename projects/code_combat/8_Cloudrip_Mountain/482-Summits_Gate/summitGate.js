// Fight your way into the Inner Sanctum of the ogre chieftain, and defeat her.

function onlyFlag() {
    var flag = hero.findFlag();
    if (flag) {
        if (hero.isReady("jump"))
            hero.jumpTo(flag.pos);
        hero.pickUpFlag(flag);
    }
}


function summonIt() {
    if (hero.canCast("summon-burl"))
        hero.cast("summon-burl");
    if (hero.canCast("summon-undead"))
        hero.cast("summon-undead");
    if (hero.canCast("raise-dead") && hero.findCorpses().length)
        hero.cast("raise-dead");
}


function summonArmy() {
    var gold = hero.gold;
    if (gold > hero.costOf("soldier"))
        hero.summon("soldier");

    var army = hero.findFriends();
    for (var i = 0; i < army.length; i++) {
        if (army[i].type == "soldier" || army[i].type == "archer") {
            var enemy = army[i].findNearestEnemy();
            if (enemy)
                hero.command(army[i], "attack", enemy);
        }
    }
}


function attackIt(enemy) {
    var distance = hero.distanceTo(enemy);
    
    if (hero.isPathClear(hero.pos, enemy.pos)) {

        if (distance < 25 && hero.canCast("fear"))
            hero.cast("fear", enemy);
        else if (distance < 30 && hero.canCast("chain-lightning"))
            hero.cast("chain-lightning", enemy);
        else if (distance < 30 && hero.canCast("poison-cloud"))
            hero.cast("poison-cloud", enemy);
        else if (distance < 15 && hero.health < hero.maxHealth / 1.5)
            hero.cast("drain-life", enemy);
        else
            hero.attack(enemy);
    }
}

function drainFriend() {
    var friend = hero.findNearest(hero.findFriends());
    if (friend && friend.type != "burl" && hero.distanceTo(friend) <= 15)
        hero.cast("drain-life", friend);
}

function battleTactics() {
    onlyFlag();
    summonIt();
    
    summonArmy();
    var enemy = hero.findNearestEnemy();
    if (enemy && enemy.type != "sand-yak")
        attackIt(enemy);
    if (hero.health < hero.maxHealth / 1.5)
        drainFriend();
}
            

while (true)
    battleTactics();

