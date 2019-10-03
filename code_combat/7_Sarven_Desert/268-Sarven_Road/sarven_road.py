while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
    else:
        hero.moveXY(hero.pos.x + 5, hero.pos.y + 5)
