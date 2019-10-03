// For this level, your hero doesn't fight.
// Command your archers to focus fire on the enemy with the most health!
function strongestEnemy(enemies) {
    var strongest = null;
    var health = 0;
    for (var i = 0; i < enemies.length; i++) {
        var enemy = enemies[i];
        if (enemy.health > health) {
            health = enemy.health;
            strongest = enemy;
        }
    }
    return strongest;
}


while (true) {
    var friends = hero.findFriends();
    var enemies = hero.findEnemies();
    var target = strongestEnemy(enemies);
    if (target)
        for (var i = 0; i < friends.length; i++)
            hero.command(friends[i], "attack", target);
}
