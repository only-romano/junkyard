from math import pi

def almostEqual(a, b):
    return abs(a - b) < 1

while True:
    skeleton = hero.findNearestEnemy()
    radius = hero.distanceTo(skeleton)
    if almostEqual(2 * pi * radius, 100):
        hero.say("Hey now now")
