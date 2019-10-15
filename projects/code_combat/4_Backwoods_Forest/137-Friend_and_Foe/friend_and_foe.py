while True:
    friend = hero.findNearestFriend()
    if friend:
        hero.say("To battle, " + friend.id + "!")
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.say("Go away, " + enemy.id + "!")
