def coinDistance():
    coin = hero.findNearestItem()
    if coin:
        return hero.distanceTo(coin)
    return 0

while True:
    distance = coinDistance()
    if distance > 0:
        hero.say(distance)
