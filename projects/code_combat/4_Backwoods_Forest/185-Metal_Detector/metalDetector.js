// The artillery uses coins as a target.
// You'll be the rangefinder for the artillery.

// Write the function.
function coinDistance() {
    // Find the nearest coin,
    var coin = hero.findNearestItem();
    // If there is a coin, return the distance to it.
    if (coin) {
        return hero.distanceTo(coin);
    }
    // Else, return 0 (zero).
    return 0;
}

while (true) {
    var distance = coinDistance();
    if (distance > 0) {
        // Say the `distance`.
        hero.say(distance);
    }
}
