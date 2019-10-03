while True:
    coin = hero.findNearestItem()
    if coin:
        hero.move(coin.pos)
    if hero.gold >= hero.costOf("soldier"):
        hero.summon("soldier")

    friends = hero.findFriends()
    for friend in friends:
        if friend.type == "soldier":
            enemy = friend.findNearestEnemy()
            if enemy:
                hero.command(friend, "attack", enemy)
            else:
                hero.command(friend, "move", {"x": 80, "y": 48})
