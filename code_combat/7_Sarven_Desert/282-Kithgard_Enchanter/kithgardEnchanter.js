// Define your own simple movement functions.
// Define moveRight
// Note: each function should move the hero 12 meters!
function moveRight() {
    var x = hero.pos.x + 12;
    var y = hero.pos.y;
    hero.moveXY(x,y);
}

// Define moveDown
function moveDown() {
    var x = hero.pos.x;
    var y = hero.pos.y - 12;
    hero.moveXY(x, y);
}
// Define moveUp
function moveUp() {
    var x = hero.pos.x;
    var y = hero.pos.y + 12;
    hero.moveXY(x, y);
}

// Now, use those functions!
moveRight();
moveDown();
moveUp();
moveUp();
moveRight();
