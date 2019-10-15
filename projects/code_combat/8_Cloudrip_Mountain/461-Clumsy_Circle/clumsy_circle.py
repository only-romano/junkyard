circleRadius = 20

def onCircle(unit, radius):
    distance = hero.distanceTo(unit)
    inaccuracy = 2
    minDistance = radius - inaccuracy
    maxDistance = radius + inaccuracy
    return distance <= maxDistance and distance >= minDistance


while True:
    soldiers = hero.findByType("soldier")
    for soldier in soldiers:
        if not onCircle(soldier, circleRadius):
            hero.say(soldier.id)
