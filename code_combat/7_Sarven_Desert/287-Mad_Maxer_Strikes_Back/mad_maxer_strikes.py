while True:
    weakest = null
    leastHealth = 99999
    enemyIndex = 0
    enemies = hero.findEnemies()

    while enemyIndex < enemies.length:
        enemy = enemies[enemyIndex]
        if enemy.health < leastHealth:
            weakest = enemy
            leastHealth = enemy.health
        enemyIndex += 1
    if weakest:
        hero.cast("drain-life", weakest)
