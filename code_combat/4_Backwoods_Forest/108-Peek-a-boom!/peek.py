while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.buildXY("fire-trap", 41, 24)
    else:
        hero.moveXY(19, 19)
