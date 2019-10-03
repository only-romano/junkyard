def findWeakestEnemy():
    enemies = hero.findEnemies()
    weakest = None
    leastHealth = 99999
    enemyIndex = 0
    while enemyIndex < len(enemies):
        enemy = enemies[enemyIndex]
        if enemy.health < leastHealth: 
            weakest = enemy
            leastHealth = enemy.health
        enemyIndex += 1

    return weakest


while True:
    weakestShaman = findWeakestEnemy()
    if weakestShaman:
        hero.attack(weakestShaman)
