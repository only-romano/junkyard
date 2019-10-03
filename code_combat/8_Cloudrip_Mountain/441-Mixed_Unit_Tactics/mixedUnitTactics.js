// Practice using modulo to loop over an array

// Choose the mix and order of units you want to summon by populating this array:
var summonTypes = false;

function summonTroops() {
    // Use % to wrap around the summonTypes array based on hero.built.length
    //var type = summonTypes[???];
    var type = "soldier";
    if (summonTypes)
        type = "archer";
    if (hero.gold >= hero.costOf(type)) {
        hero.summon(type);
        summonTypes = !summonTypes;
    }
}


function commandAll() {
    var friends = hero.findFriends();
    for (var i = 0; i < friends.length; i++) {
        var friend = friends[i];
        if (friend.type == "archer" || friend.type == "soldier") {
            var enemy = friend.findNearestEnemy();
            if (enemy)
                hero.command(friend, "attack", enemy);
        }
    }
}


function collectGold() {
    var coin = hero.findNearestItem();
    if (coin)
        hero.move(coin.pos);
}


while (true) {
    collectGold();
    summonTroops();
    commandAll();
}
