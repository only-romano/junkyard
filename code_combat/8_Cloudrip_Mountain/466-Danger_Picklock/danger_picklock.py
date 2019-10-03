from math import pi

def almostEqual(a, b):
    return abs(a - b) < (b * 0.05)


bomb = hero.findByType("robobomb")[0]
wizards = hero.findByType("wizard")
chargeArea = bomb.chargeArea
while True:
    radius = bomb.distanceTo(wizards[0])
    area = pi * radius * radius
    if almostEqual(area, chargeArea):
        hero.say("Boom!")
