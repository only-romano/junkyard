// Robobombs explode when they are destroyed or touch an enemy.
// Split up your soldiers so that they don't all get exploded together.

while(true) {
    var enemies = hero.findEnemies();
    var enemy = hero.findNearest(enemies);
    var friends = hero.findFriends();
    // Send the first soldier of the friends array towards the enemy.
    hero.command(friends[0], "attack", enemy);
    // i = 1 starts the index at the second element!
    for(var i = 1; i < friends.length; i++) {
        var friend = friends[i];
        // Command the remaining soldiers to run away!
        hero.command(friend, "move", {"x": 11, "y": 20});
    }
}
