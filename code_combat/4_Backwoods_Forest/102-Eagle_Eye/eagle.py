while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
