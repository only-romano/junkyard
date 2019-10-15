// Pick up coins only if they are closer than 20m.
// Pick up all gems.

while (true) {
    var item = hero.findNearestItem();
    var distance = hero.distanceTo(item);
    // If the item's type is "gem"
    // OR the distance to the item less than 20 meters:
    if (item.type == "gem" || hero.distanceTo(item) < 20) {
        // Move to item's position.
        hero.moveXY(item.pos.x, item.pos.y);
    }
        
}
