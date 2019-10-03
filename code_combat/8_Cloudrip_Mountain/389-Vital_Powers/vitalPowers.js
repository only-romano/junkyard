// This level shows how to define your own functions.
// The code inside a function is not executed immediately. It's saved for later.
// This function has your hero collect the nearest coin.
function pickUpNearestCoin() {
    var items = hero.findItems();
    var nearestCoin = hero.findNearest(items);
    if(nearestCoin) {
        hero.move(nearestCoin.pos);
    }
}

// This function has your hero summon a soldier.
function summonSoldier() {
    // If hero.gold is greater than the cost of the "soldier":
    if (hero.gold > hero.costOf("soldier"))
        // Then summon a "soldier":
        hero.summon("soldier");
}

// This function commands your soldiers to attack their nearest enemy.
function commandSoldiers() {
    var friends = hero.findFriends();
    for(var i=0; i < friends.length; i++) {
        var enemy = friends[i].findNearestEnemy();
        var friend = friends[i];
        if(enemy && friend.type == "soldier") {
            hero.command(friends[i],"attack", enemy);
        }
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

while(true) {
    // In your loop, you can "call" the functions defined above.
    // The following line causes the code inside the "pickUpNearestCoin" function to be executed.
    pickUpNearestCoin();
    // Call summonSoldier here
    summonSoldier();
    // Call commandSoldiers here
    commandSoldiers();
    summonIt();
}
