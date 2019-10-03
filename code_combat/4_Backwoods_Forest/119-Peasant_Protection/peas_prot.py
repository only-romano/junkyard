while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        distance = hero.distanceTo(enemy)
        if distance < 20:
            hero.attack(enemy)
        else:
            hero.moveXY(40, 37)
