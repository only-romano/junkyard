while True:
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 10:
        hero.cleave(nearestEnemy)
    else:
        hero.attack("Chest")
