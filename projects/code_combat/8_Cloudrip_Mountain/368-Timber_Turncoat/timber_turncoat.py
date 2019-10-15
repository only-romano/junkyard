while True:
    var coin = hero.findNearestItem()
    if coin:
        hero.move(coin.pos)
    if hero.gold >= hero.costOf("soldier"):
        hero.summon("soldier")
    friends = hero.findFriends()
    heal = []

    for friend in friends:
        if friend.type == "soldier":
            enemy = friend.findNearestEnemy()
            if enemy:
                if friend.health < 100:
                    hero.command(friend, "move", {"x": 20, "y": 48})
                    heal.push(friend)
                else:
                    hero.command(friend, "attack", enemy)
            else:
                hero.command(friend, "move", {"x": 80, "y": 48})

    if hero.canCast("regen"):
        for man in heal:
            if hero.distanceTo(man) <= 30:
                hero.cast("regen", man)
                break
