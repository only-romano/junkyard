while True:
    if hero.canCast("regen"):
        bernardDistance = hero.distanceTo("Bernard")
        if bernardDistance < 10:
            hero.cast("regen", "Bernard")

        chandraDistance = hero.distanceTo("Chandra")
        if chandraDistance < 10:
            hero.cast("regen", "Chandra")
    else:
        enemy = hero.findNearestEnemy()
        if enemy and hero.distanceTo(enemy) <= hero.attackRange:
            hero.attack(enemy);
