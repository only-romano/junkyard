while True:
    enemies = hero.findEnemies()
    enemyIndex = 0

    while enemyIndex < len(enemies):
        enemy = enemies[enemyIndex]
        if enemy.type != "sand-yak":
            while enemy.health > 0:
                if hero.isReady("bash"):
                    hero.bash(enemy)
                else:
                    hero.attack(enemy)
        enemyIndex += 1

    hero.moveXY(40, 32)
