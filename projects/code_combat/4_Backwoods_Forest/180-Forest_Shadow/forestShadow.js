// Big ogres can't see you in the forest.
// Attack only the small ogres in the forest.
// Collect coins and gems only.
// Don't leave the forest and don't eat/drink anything.

while (true) {
    // Find the nearest enemy.
    var enemy = hero.findNearestEnemy();
    // Attack it only if its type is "thrower" or "munchkin".
    if (enemy.type == "thrower" || enemy.type == "munchkin") {
        hero.attack(enemy);
    }
    // Find the nearest item.
    var item = hero.findNearestItem();
    // Collect it only if its type is "gem" or "coin".
    if (item.type == "gem" || item.type == "coin") {
       hero.moveXY(item.pos.x, item.pos.y);
    }
}
