while True:
    enemy = hero.findNearestEnemy()

    if enemy.type == "munchkin" or enemy.type == "thrower":
        hero.attack(enemy)

    if enemy.type == "ogre":
        hero.moveXY(41, 47)
