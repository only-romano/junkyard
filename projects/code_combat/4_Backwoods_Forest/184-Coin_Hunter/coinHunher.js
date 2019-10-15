// To make the training more interesting Senick poisoned you.
// While you aren't moving the poison is harmless.

// This function should check if a coin is closer than 20m.
function isCoinClose(coin) {
    // Find the distance to the `coin`.
    var distance = hero.distanceTo(coin);
    // If the distance is less than 20: 
    if (distance < 20) {
        // Return true
        return true;
    }
    // Else:
    else
        // Return false
        return false;
}

while (true) {
    var item = hero.findNearestItem();
    if (item) {
        // If isCoinClose(item) returns true:
        if (isCoinClose(item)) {
            hero.moveXY(item.pos.x, item.pos.y);
        }
    }
}
