while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    
    if flag:
        hero.pickUpFlag(flag)
    elif enemy:
        if hero.distanceTo(enemy) < 10:
            if hero.isReady("cleave"):
                hero.cleave(enemy)
            else:
                hero.attack(enemy)
