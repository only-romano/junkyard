// Gather coins to summon soldiers and have them attack the enemy.

while(true) {
    // Move to the nearest coin.
    // Use move instead of moveXY so you can command constantly.
    var coin = hero.findNearestItem();
    if (coin)
        hero.move(coin.pos);
    
    // If you have funds for a soldier, summon one.
    if (hero.gold > hero.costOf("soldier")) {
        hero.summon("soldier");
    }
    var enemy = hero.findNearest(hero.findEnemies());
    if (enemy) {
        
        var soldiers = hero.findFriends();
        var soldierIndex = 0;
        while (soldierIndex < soldiers.length) {
            var soldier = soldiers[soldierIndex];
        // Loop over all your soldiers and order them to attack.
            // Use the 'attack' command to make your soldiers attack.
            hero.command(soldier, "attack", enemy);
            soldierIndex += 1;
        }
    }
}
