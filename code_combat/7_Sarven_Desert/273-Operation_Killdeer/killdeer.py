def shouldRun():
    return hero.health < hero.maxHealth / 2

while True:
    if shouldRun():
        hero.moveXY(75, 37)
    else:
        enemy = hero.findNearestEnemy()
        if (enemy):
            hero.attack(enemy)
