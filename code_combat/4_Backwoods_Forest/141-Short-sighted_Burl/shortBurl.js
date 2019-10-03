// Collect coins and run, or else the burl will find you.

// This function allows your hero take an item.
function takeItem(item) {
    hero.moveXY(item.pos.x, item.pos.y);
}

// Write the function "checkTakeRun" with one parameter.
// If the item exists, use "takeItem" function to take it.
// Go back to the start (green mark), with or without the item.
function checkTakeRun(item) {
    if (item) {
        takeItem(item);
    }
    hero.moveXY(40, 13);
}

// Don't change this code.
while (true) {
    hero.moveXY(16, 56);
    var coin = hero.findNearestItem();
    checkTakeRun(coin);
    
    hero.moveXY(64, 56);
    coin = hero.findNearestItem();
    checkTakeRun(coin);
}
