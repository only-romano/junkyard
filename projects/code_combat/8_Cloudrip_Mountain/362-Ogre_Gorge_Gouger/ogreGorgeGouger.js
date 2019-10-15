// You only have 20 seconds until the ogre horde arrives!
// Grab as much gold as you can, then retreat to your base and wall it off!
function bestCoin(arr) {
    var bestValue = 0;
    var best = null;
    for (var i = 0; i < arr.length; i++) {
        var coin = arr[i];
        var profit = coin.value / hero.distanceTo(coin);
        if (profit > bestValue) {
            bestValue = profit;
            best = coin;
        }
    }
    return best;
}

var coin = bestCoin(hero.findItems());
while(hero.time < 20 && coin) {
    // Collect coins
    hero.move(coin.pos);
    coin = bestCoin(hero.findItems());
}

while(hero.pos.x > 16) {
    // Retreat behind the fence
    hero.move({"x": 16, "y": 38});
}

// Build a fence to keep the ogres out.
hero.buildXY("fence", 21, 37);
