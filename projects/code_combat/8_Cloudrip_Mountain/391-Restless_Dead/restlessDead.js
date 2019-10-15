// This level is supposed to be VERY hard! You may need a great strategy
// and or gear to complete it!

// Find and defeat the yeti then gather its essence for the ritual.
// You might want to gather the coins the yeti leaves behind,
// you'll need them to summon an army
// Stand at the summoning stone (red x) to begin summoning
// Now you just have to survive the undead hoard


function onlyFlag() {
    var flag = hero.findFlag();
    if (flag) {
        if (hero.isReady("jump"))
            hero.jumpTo(flag.pos);
        else
            hero.moveXY(flag.pos.x, flag.pos.y);
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
        if (army[i].type == "soldier") {
            var enemy = army[i].findNearestEnemy();
            if (enemy)
                hero.command(army[i], "attack", enemy);
        }
    }
}


function attackIt(enemy) {
    var distance = hero.distanceTo(enemy);
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

function drainFriend() {
    var friend = hero.findNearest(hero.findFriends());
    if (friend && friend.type != "burl" && hero.distanceTo(friend) <= 15)
        hero.cast("drain-life", friend);
}

function getBestCoin() {
    var coins = hero.findItems();
    var best = null;
    var value = 0;
    for (var i = 0; i < coins.length; i++) {
        var now = coins[i].value / hero.distanceTo(coins[i]);
        if (now > value){
            value = now;
            best = coins[i];
        }
    }
    return best;
}

function battleTactics() {
    onlyFlag();
    summonIt();
    
    var coin = getBestCoin();
    if (coin)
        hero.move(coin.pos);
    summonArmy();
    var enemy = hero.findNearestEnemy();
    if (enemy)
        attackIt(enemy);

    if (hero.health < hero.maxHealth / 2)
        drainFriend();
}
            

while (true)
    battleTactics();
