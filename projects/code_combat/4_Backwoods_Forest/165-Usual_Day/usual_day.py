while True:
    enemy = hero.findNearestEnemy()
    if enemy and enemy.type == "munchkin":
        hero.attack(enemy)
    item = hero.findNearestItem()
    if item and item.type == "coin":
        hero.moveXY(item.pos.x, item.pos.y)
