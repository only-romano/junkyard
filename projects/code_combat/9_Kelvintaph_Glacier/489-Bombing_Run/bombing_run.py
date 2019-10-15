from math import pi, atan2

while True:
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 60:
        x = abs(enemy.pos.x - hero.pos.x)
        y = abs(enemy.pos.y - hero.pos.y)
        angle = atan2(y, x)
        angle = angle * 180 / pi
        if enemy.pos.x < hero.pos.x:
            angle = 180 - angle
        hero.say(angle)
