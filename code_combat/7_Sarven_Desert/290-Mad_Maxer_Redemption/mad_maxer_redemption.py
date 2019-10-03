while True:
    weakestFriend = None
    leastHealth = 9999
    friendIndex = 0
    friends = hero.findFriends()
    while friendIndex < len(friends):
        friend = friends[friendIndex]
        friendIndex += 1
        if friend.health < leastHealth:
            weakestFriend = friend
            leastHealth = friend.health
    if weakestFriend:
        hero.say('Hey ' + weakestFriend.id + ', go home!')
