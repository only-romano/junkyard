while True:
    if hero.canCast("haste"):
        hero.cast("haste", hero)
    item = hero.findNearestItem()
    if item and item.type != "gem":
        if hero.isReady("jump"):
            hero.jumpTo(item.pos)
        else:
            hero.moveXY(item.pos.x, item.pos.y)

    enemy = hero.findNearestEnemy()
    if enemy and enemy.type != "burl":
        hero.attack(enemy)
