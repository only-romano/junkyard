// You can use findNearestEnemy() on your soldiers to get their nearest enemy instead of yours.
while (true) {
    var friends = hero.findFriends();
    // Use for-loop and for each friend:
    for (var i = 0; i < friends.length; i++) {
        // If they see an enemy then command to attack.
        var friend = friends[i];
        var enemy = friend.findNearestEnemy();
        if (enemy && friend.distanceTo(enemy) < 30)
            hero.command(friend, "attack", enemy);
        // Command to move east by small steps.
        else
            hero.command(friend, "move", {"x": friend.pos.x + 2, "y": friend.pos.y});
    }
}
