while True:
    enemy = hero.findNearestEnemy()
    if enemy and enemy.health > 0:
        if hero.isReady("bash"):
            hero.bash(enemy)
            hero.moveXY(40, 33)
        else:
            hero.shield()
    else:
        hero.moveXY(18, 9)
        hero.moveXY(66, 58)
        hero.moveXY(40, 33)
        hero.moveXY(63, 14)
        hero.moveXY(15, 56)
