enemies = hero.findEnemies()
enemyIndex = 0

while enemyIndex < len(enemies):
    enemy = enemies[enemyIndex]
    if enemy.type == 'shaman':
        while enemy.health > 0:
            hero.attack(enemy)
    enemyIndex++;
