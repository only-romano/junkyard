while True:
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)
    if enemy.type == "munchkin" and distance < 20:
        hero.attack(enemy)
