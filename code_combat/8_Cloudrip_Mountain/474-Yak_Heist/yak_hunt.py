def averageSize(yaks):
    total = 0
    for yak in yaks:
        total += yak.size
    return total / yaks.length

yaks = hero.findEnemies()
avgSize = averageSize(yaks)

bestYak = None
closestDist = 9999
for yak in yaks:
    yak = yaks[i]
    yakDistance = hero.distanceTo(yak)
    yakSize = yak.size
    if yakDistance < closestDist and yakSize > avgSize:
        bestYak = yak
        closestDist = yakDistance

hero.say(bestYak)
