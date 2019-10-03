// Destroy mechs and collect gold from them.

while (true) {
    var coin = hero.findNearestItem();
    // While a coin exists:
    while (coin) {
        // Move to the coin.
        hero.moveXY(coin.pos.x, coin.pos.y);
        // Reassign the coin variable to the nearest item.
        coin = hero.findNearestItem();
    }
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        // While enemy's health is greater than 0.
        while (enemy.health > 0) {
            // Attack enemy.
            if (hero.isReady("bash")) hero.bash(enemy);
            else hero.attack(enemy);
        }
    }
}
