def goTo(x, y, message):
    hero.moveXY(x, y)
    hero.say(message)
    return message

hero.cast("haste", hero)
hero.moveXY(18, 20)
secret = hero.findNearestFriend().getSecret()

goTo(38, 37, secret/4 - goTo(42, 20, goTo(30, 15, secret/4)/5))
