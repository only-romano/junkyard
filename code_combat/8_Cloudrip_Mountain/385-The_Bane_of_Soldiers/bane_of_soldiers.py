while True:
    friends = hero.findFriends()
    hero.command(friends[0], "attack", hero.findNearest(hero.findEnemies()))
    for i in range(1, len(friends)):
        hero.command(friends[i], "move", {"x": 11, "y": 20})
