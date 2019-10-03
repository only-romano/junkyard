while True:
    friends = hero.findFriends()
    for friend in friends:
        enemy = friend.findNearestEnemy()
        if enemy and friend.distanceTo(enemy) < 30:
            hero.command(friend, "attack", enemy)
        else:
            hero.command(friend, "move", {"x": friend.pos.x + 2, "y": friend.pos.y})
