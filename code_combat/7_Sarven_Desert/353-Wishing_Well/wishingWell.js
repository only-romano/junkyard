// You need exactly 104 gold. 

var less = "Nimis";
var more = "Non satis";
var requiredGold = 104;

// This function calculates the sum of all coin values.
function sumCoinValues(coins) {
    var coinIndex = 0;
    var totalValue = 0;
    // Iterate all coins.
    while (coinIndex < coins.length) {
        totalValue += coins[coinIndex].value;
        coinIndex++;
    }
    return totalValue;
}

function collectAllCoins() {
    var item = hero.findNearest(hero.findItems());
    while (item) {
        hero.moveXY(item.pos.x, item.pos.y);
        item = hero.findNearest(hero.findItems());
    }
}

while (true) {
    var items = hero.findItems();
    // Get the total value of coins.
    var goldAmount = sumCoinValues(items);
    // If there are coins, then goldAmount isn't zero.
    if (goldAmount !== 0) {
        // If goldAmount is less than requiredGold
        if (goldAmount < requiredGold) {
            // Then say "Non satis".
            hero.say("Non satis");
        }
        // If goldAmount is greater than requiredGold
        else if (goldAmount > requiredGold) {
            // Then say "Nimis".
            hero.say("Nimis");
        }
        // If goldAmount is exactly equal to requiredGold
        else {
            // Then collect all coins:
            collectAllCoins();
        }
    }
}
