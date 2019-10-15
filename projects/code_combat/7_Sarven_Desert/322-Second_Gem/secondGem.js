// One gem is safe, the others are bombs.
// But you know the answer: always take the second.

while (true) {
    var items = hero.findItems();
    // If the length of items is greater or equal to 2:
    if (items.length >= 2) {
        // Move to the second item in items
        var second = items[1].pos;
        hero.moveXY(second.x, second.y);
    }
    // Else:
    else {
        // Move to the center mark.
        hero.moveXY(40, 34);
    }
}
