while True:
    currentHealth = hero.health
    if currentHealth < hero.maxHealth / 2:
        hero.moveXY(65, 46)

    enemy = hero.findNearestEnemy()
    if enemy:
        distance = hero.distanceTo(enemy)
        if currentHealth < hero.maxHealth and hero.canCast("drain-life") && distance <= 15:
            hero.cast("drain-life", enemy)
        elif hero.canCast("chain-lightning") and distance <= 30:
            hero.cast("chain-lightning", enemy)
        else:
            hero.attack(enemy)
