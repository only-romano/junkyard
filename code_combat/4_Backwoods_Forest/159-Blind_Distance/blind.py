def nearestEnemyDistance():
    enemy = hero.findNearestEnemy()
    result = 0
    if enemy:
        result = hero.distanceTo(enemy)

    return result

while True:
    enemyDistance = nearestEnemyDistance()
    if enemyDistance > 0:
        hero.say(enemyDistance)
