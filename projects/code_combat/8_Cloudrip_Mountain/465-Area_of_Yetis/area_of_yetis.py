from math import pi

hero.say(hero.findFriends()[0].distanceTo(chosen.findNearestEnemy())**2 * pi)

while True:
    enemy = hero.findNearest(hero.findByType("yeti"))
    if enemy:
        hero.attack(enemy)
