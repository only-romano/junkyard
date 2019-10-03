while True:
    enemy = hero.findNearestEnemy()
    if enemy and enemy.type != "peon":
        hero.attack(enemy)

    item = hero.findNearestItem()
    if item and item.type != "poison":
        hero.moveXY(item.pos.x, item.pos.y)
