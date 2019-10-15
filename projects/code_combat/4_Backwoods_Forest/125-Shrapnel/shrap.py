while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        if hero.isReady("throw"):
            distance = hero.distanceTo(enemy)
            if distance > 15:
                hero.throw(enemy)
            else:
                hero.attack(enemy)
        else:
            hero.attack(enemy)
