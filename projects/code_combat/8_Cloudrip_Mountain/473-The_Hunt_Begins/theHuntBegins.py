def averageSize(burls):
    return sumSize(burls) / burls.length


def sumSize(burls):
    total = 0
    for burl in burls:
        total += burl.size
    return total


while True:
    hero.say(averageSize(hero.findEnemies()))
