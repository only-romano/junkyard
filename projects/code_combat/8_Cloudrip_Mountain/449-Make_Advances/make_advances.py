while True:
    friends = hero.findFriends()
    projectiles = hero.findEnemyMissiles()
    for friend in friends:
        if friend.type == "paladin":
            projectile = friend.findNearest(projectiles)
            if projectile and friend.distanceTo(projectile) < 10:
                hero.command(friend, "shield")
            else:
                hero.command(friend, "move", {"x": friend.pos.x + 10, "y": friend.pos.y})
        else:
            hero.command(friend, "move", {"x": friend.pos.x + 1, "y": friend.pos.y})
    hero.move({"x": hero.pos.x + 5, "y": hero.pos.y})
