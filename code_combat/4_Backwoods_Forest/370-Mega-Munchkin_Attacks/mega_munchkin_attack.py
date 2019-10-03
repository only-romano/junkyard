while True:
    friend = hero.findNearest(hero.findFriends())
    enemy = hero.findNearest(hero.findEnemies())

    if friend and enemy:
        hero.command(friend, "attack", enemy)
        if friend.pos.x + 8 > enemy.pos.x:
            hero.command(friend, "move", {"x": enemy.pos.x - 15, "y": friend.pos.y - 7})
