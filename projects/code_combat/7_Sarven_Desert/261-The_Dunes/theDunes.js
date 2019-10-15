// Collect coins. Ignore "sand-yak"s and "burl"s.

while (true) {
    var enemy = hero.findNearestEnemy();
    var item = hero.findNearestItem();
    if (enemy) {
        if (enemy.type == "sand-yak" || enemy.type == "burl") {
            // Don't attack! Collect coins.
            if (item) {
                hero.moveXY(item.pos.x, item.pos.y);
            }
        } else {
            // Else, attack. 
            hero.attack(enemy);
        }
    } else if (item) {
        // Collect coins: move to item's position.
        hero.moveXY(item.pos.x, item.pos.y);
    } else {
        hero.moveXY(41, 31);
    }
}
