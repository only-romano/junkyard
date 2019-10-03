def findFurthestEnemy():
    enemies = hero.findEnemies()
    furthestEnemy = None
    maxDistance = 0
    for enemy in enemies:
        distance = hero.distanceTo(enemy)
        if distance > maxDistance:
            furthestEnemy = enemy
            maxDistance = distance
    return furthestEnemy


while True:
    furthestOgre = findFurthestEnemy()
    if furthestOgre:
        while furthestOgre.health > 0:
            hero.attack(furthestOgre)
