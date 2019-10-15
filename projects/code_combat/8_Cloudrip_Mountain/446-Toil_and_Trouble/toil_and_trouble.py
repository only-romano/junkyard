def chooseTarget(friend):
    if friend.type == "soldier":
        enemy = friend.findNearest(hero.findByType("witch"))
        if enemy:
            return enemy
    return friend.findNearestEnemy()


while True:
    friends = hero.findFriends()
    for friend in friends:
        enemy = chooseTarget(friend)
        if enemy:
            hero.command(friend, "attack", enemy)
