// Defeat all incoming ogres.

while(true) {
    // Find the nearest enemy.
    var enemy = hero.findNearestEnemy();
    // If there is an enemy, and it is a "brawler":
    if (enemy && enemy.type == "brawler")
        // Then say its name (.id) in UPPERCASE.
        hero.say(enemy.id.toUpperCase());
    // For other enemies, just fight.
    else if (enemy)
        hero.attack(enemy);
}
