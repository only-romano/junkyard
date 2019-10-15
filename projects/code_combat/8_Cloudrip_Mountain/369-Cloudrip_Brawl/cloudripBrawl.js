// Stay alive for one minute.
// If you win, the next time you play will be more difficult and more rewarding!
// If you lose, you must wait a day before submitting again.

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
        if (army[i].type == "soldier") {
            var enemy = army[i].findNearestEnemy();
            if (enemy)
                hero.command(army[i], "attack", enemy);
        }
    }
}

/*
function attackIt(enemy) {
    var distance = hero.distanceTo(enemy)

    if distance < 25 and hero.canCast("fear"):
        hero.cast("fear", enemy)
    elif distance < 30 and hero.canCast("chain-lightning"):
        hero.cast("chain-lightning", enemy)
    elif distance < 30 and hero.canCast("poison-cloud"):
        hero.cast("poison-cloud", enemy)
    elif distance < 15 and hero.health < hero.maxHealth / 1.5:
        hero.cast("drain-life", enemy)
    else:
        hero.attack(enemy)
}
*/
/*
def drainFriend():
    friend = hero.findNearest(hero.findFriends())
    if friend and friend.type != "burl" and hero.distanceTo(friend) <= 15:
        hero.cast("drain-life", friend)
*/

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
/*
    var enemy = hero.findNearestEnemy();
    if (enemy and enemy.type != "sand-yak":
        attackIt(enemy)

    if (hero.health < hero.maxHealth / 2)
        drainFriend();*/
}
            

while (true)
    battleTactics();

