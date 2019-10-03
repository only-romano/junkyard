while True;
    enemy = hero.findNearestEnemy()
    if enemy:
        distance = hero.distanceTo(enemy)
        if distance < hero.throwRange:
            hero.throw(enemy)
        else:
            hero.attack(enemy)
