// Collect 10 real coins.

while (true) {
    var coins = hero.findItems();
    // if (coins.length) {
        // The following code will help you debug:
        // var coin = coins[0];
        // hero.say(coin.value);
        // hero.moveXY(coin.pos.x, coin.pos.y);
        // When ready, delete the previous code and solve.
    // }
    if (!coins.length)
        continue;
    var unique = null;

    for (var i = 0; i < coins.length; i++) {
        unique = coins[i];
        for (var j = 0; j < coins.length; j++) {
            if (i == j)
                continue;
            if (coins[i].value == coins[j].value) {
                unique = null;
                break;
            }
        }
        if (unique)
            break;
    }
    if (unique)
        hero.moveXY(unique.pos.x, unique.pos.y);
}
