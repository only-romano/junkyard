// Collect mushrooms.

// First, come to the wolf pet and wake up it (say).
hero.moveXY(12, 34);
hero.say("Wake up, wolf!");
// Next collect mushrooms just usual items.
while(true) {
    var item = hero.findNearestItem();
    if (item) {
        hero.moveXY(item.pos.x, item.pos.y);
    }
}
