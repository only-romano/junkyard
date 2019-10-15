while True:
    farthest = None
    maxDistance = 0
    enemies = hero.findEnemies()

    for enemy in enemies:
        distance = hero.distanceTo(enemy)
        if distance > maxDistance:
            maxDistance = distance
            farthest = enemy

    if farthest:
        while farthest.health > 0:
            hero.attack(farthest)
