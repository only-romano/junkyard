while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        distance = hero.distanceTo(enemy)
        if distance < 15:
            hero.cast("drain-life", enemy)
        else:
            hero.attack(enemy)
