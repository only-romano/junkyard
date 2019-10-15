// Collect exactly 7 spinach potions.
// Then you'll be strong enough to defeat the ogres.

var potionCount = 0;

// Wrap the potion collection code inside a while loop.
// Use a condition to check the potionCount
while (potionCount != 7) {
    var item = hero.findNearestItem();
    if (item) {
        hero.moveXY(item.pos.x, item.pos.y);
        potionCount++;
    }
}

// When the while loop is finished,
// Go and fight!
while (true) {
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        hero.attack(enemy);
    }
}
