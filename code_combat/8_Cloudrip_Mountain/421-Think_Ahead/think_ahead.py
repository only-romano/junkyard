def findNearestPair(units):
    minDistance = 9001
    nearestPair = ["Nobody", "Nobody"]
    for i in range(len(units)):
        for j in range(len(units)):
            if i == j:
                continue
            dist = units[i].distanceTo(units[j])
            if dist < minDistance:
                minDistance = dist
                nearestPair = [units[i].id, units[j].id]
    return nearestPair


while True:
    if hero.time % 8 == 5:
        pairOfNames = findNearestPair(hero.findByType("soldier"))
        hero.say(pairOfNames[0] + " " + pairOfNames[1])
