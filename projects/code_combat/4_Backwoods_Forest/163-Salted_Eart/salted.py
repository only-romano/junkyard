while True:
    enemy = hero.findNearestEnemy()
    if enemy.type == "munchkin" or enemy.type == "thrower":
        hero.attack(enemy)

    item = hero.findNearestItem()
    if item.type == "gem" or item.type == "coin":
        hero.moveXY(item.pos.x, item.pos.y)
