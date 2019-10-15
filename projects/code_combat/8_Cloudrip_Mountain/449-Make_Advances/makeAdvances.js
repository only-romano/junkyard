// Advance through the forgotten tomb.
// Be wary, traps lay in wait to ruin your day!

// The Paladins volunteer to lead the way.
// Command them to shield against incoming projectiles.
while(true) {
    var friends = hero.findFriends();
    // findEnemyMissiles finds all dangerous projectiles.
    var projectiles = hero.findEnemyMissiles();
    for(var i = 0; i < friends.length; i++) {
        var friend = friends[i];
        if(friend.type == "paladin") {
            // Find the projectile nearest to the friend:
            var projectile = friend.findNearest(projectiles);
            // If the projectile exists
            // AND is closer than 10 meters to the paladin:
            if (projectile && friend.distanceTo(projectile) < 10)
                // Command the friend to "shield":
                hero.command(friend, "shield");
            // ELSE, when there is no potential danger:
            else
                // Advance the paladin:
                hero.command(friend, "move", {x: friend.pos.x + 10, y: friend.pos.y});
        } else {
            // If not a paladin, just advance:
            hero.command(friend, "move", {x: friend.pos.x + 1, y: friend.pos.y});
        }
    }
    // Advance the hero in the x direction:
    hero.move({x: hero.pos.x + 5, y: hero.pos.y});
}
