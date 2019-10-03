// Collect all the coins!

function commandPeasant(peasant, coins) {
    // Find the nearest coin to the `peasant` from the `coins` array,
    var coin = peasant.findNearest(coins);
    // Command the peasant "move" to the nearest coin.
    if (coin)
        hero.command(peasant, "move", coin.pos);
}

var friends = hero.findFriends();
var peasants = {
    "Aurum":friends[0],
    "Argentum":friends[1],
    "Cuprum":friends[2]
};

while(true) {
    var items = hero.findItems();
    var goldCoins = [];
    var silverCoins = [];
    var bronzeCoins = [];
    for(var i = 0; i < items.length; i++) {
        var item = items[i];
        if(item.value == 3) {
            goldCoins.push(item);
        }
        // Put bronze and silver coins in their approriate array:
        else if (item.value == 2) {
            silverCoins.push(item);
        }
        else if (item.value == 1) {
            bronzeCoins.push(item);
        }
    }
    commandPeasant(peasants.Aurum, goldCoins);
    commandPeasant(peasants.Argentum, silverCoins);
    commandPeasant(peasants.Cuprum, bronzeCoins);
}
