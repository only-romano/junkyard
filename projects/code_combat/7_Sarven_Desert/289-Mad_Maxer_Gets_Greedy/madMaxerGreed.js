// Collect more coins than your doppelganger.
// You only have a few seconds to collect coins. Choose your path wisely!
while(true) {
    var bestCoin = null;
    var maxRating = 0;
    var coinIndex = 0;
    var coins = hero.findItems();
    // Try calculating "value / distance" to decide which coins to get.
    while (coinIndex < coins.length) {
        var gold = coins[coinIndex++];
        var rating = gold.value / hero.distanceTo(gold);
        if (rating > maxRating && gold.pos.x < 40) {
            maxRating = rating;
            bestCoin = gold;
        }
    }
    if (bestCoin)
        hero.moveXY(bestCoin.pos.x, bestCoin.pos.y);
}
