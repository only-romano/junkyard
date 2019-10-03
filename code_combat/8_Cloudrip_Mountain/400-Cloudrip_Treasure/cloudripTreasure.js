// Your goal is to collect coins / gems.
// This level is repeatable. If you win, the difficulty and rewards will increase.
// If you fail, you have to wait a day to resubmit.
// This level is an optional challenge level. You don't need to beat it to continue the campaign!

function onSpawn() {
    while (true) {
        pet.moveXY(25, 60);
        pet.moveXY(25, 100);
        pet.moveXY(25, 25);
        pet.moveXY(25, 60);
        pet.moveXY(125, 60);
        pet.moveXY(125, 100);
        pet.moveXY(125, 25);
        pet.moveXY(125, 60);
    }
}


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


function findBestItem(friend, excludedItems) {
    var items = friend.findItems();
    var bestItem = null;
    var bestItemValue = 0;
    for(var i = 0; i < items.length; i++) {
        var item = items[i];
        var idx = excludedItems.indexOf(item);
        if(idx != -1) { continue; }
        var value = item.value / friend.distanceTo(item);
        if (value > bestItemValue) {
            bestItem = item;
            bestItemValue = value;
        }
    }
    return bestItem;
}


function peasants() {
    var peasants = hero.findByType("peasant");
    var claimedItems = [];
    for(var i = 0; i < peasants.length; i++) {
        var peasant = peasants[i];
        var item = findBestItem(peasant, claimedItems);
        if(item) {
            claimedItems.push(item);
            hero.command(peasant, "move", item.pos);
        }
    }
}


function summonIt() {
    if (hero.canCast("summon-burl"))
        hero.cast("summon-burl");
    else if (hero.isReady("reset-cooldown"))
        hero.resetCooldwon("summon-burl");
    if (hero.canCast("summon-undead"))
        hero.cast("summon-undead");
    if (hero.canCast("raise-dead") && hero.findCorpses().length)
        hero.cast("raise-dead");
}


function summonArmy() {
    var gold = hero.gold;
    if (gold >= hero.costOf("soldier")) {
        if (type == 1 && gold >= hero.costOf("archer")) {
            hero.summon("archer");
            type = 0;
        } else {
            hero.summon("soldier");
            type = 1;
        }
    }

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


pet.on("spawn", onSpawn);
var type = 1;

while(true) {
    onlyFlag();
    peasants();
    summonIt();
    summonArmy();
    var enemy = hero.findNearestEnemy();
    if (enemy)
        attackIt(enemy);

    if (hero.health < hero.maxHealth / 2)
        drainFriend();
}
