// Collect 10 gems.

// Use "blink" ability to teleport between gaps.
while(true) {
    // hero.blink(Vector(x, y));
    // hero.blink(thing.pos);
    var item = hero.findNearestItem();
    if (item) {
        var x = item.pos.x;
        var y = item.pos.y;
        hero.blink(Vector(x, y));
    }
}
