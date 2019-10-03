// Coins here disappear after a few seconds!
// Get all the gold coins before they vanish.

while(true) {
    var closestGold = null;
    var minGoldDist = Infinity;
    var coinIndex = 0;
    var coins = hero.findItems();
    // Find the closest coin that is gold.
    // Remember that gold coins have a value of 3.
    while (coinIndex < coins.length) {
        var gold = coins[coinIndex++];
        if (gold.value !== 3) continue;
        var distance = hero.distanceTo(gold);
        if (distance < minGoldDist) {
            minGoldDist = distance;
            closestGold = gold;
        }
    }
    if(closestGold) {
        // Now go to the closest gold coin and get it!
        hero.moveXY(closestGold.pos.x, closestGold.pos.y);
    }
}
