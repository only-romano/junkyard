while True:
    enemy = hero.findNearestEnemy();
    if enemy:
        if hero.isReady("cleave"):
            hero.cleave(enemy)
        else:
            hero.attack(enemy)
