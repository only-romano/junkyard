// Wonderglade has changed since our last visit.
// Ogres cursed it and we should defeat them.
// The burl still is collecting gems, so don't touch them.
// Also don't attack the burl.

while (true) {
    // Find the nearest item.
    // Collect it (if it exists) only if its type isn't "gem".
    var item = hero.findNearestItem();
    if (item && item.type != "gem") {
        hero.moveXY(item.pos.x, item.pos.y);
    }
    // Find the nearest enemy.
    // Attack it if it exists and its type isn't "burl".
    var enemy = hero.findNearestEnemy();
    if (enemy && enemy.type != "burl") {
        hero.attack(enemy);
    }
}
