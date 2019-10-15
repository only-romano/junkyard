// You need to collect several items.
// But, the burl wants the gems!
// Pick up all appearing items EXCEPT gems.

while (true) {
    var item = hero.findNearestItem();
    if (item) {
        // If item.type isn't equal to "gem":
        if (item.type != "gem") {
            // Move to the item's position.
            hero.moveXY(item.pos.x, item.pos.y);
        }
    }
}
