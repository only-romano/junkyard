while True:
    enemies = hero.findEnemies()
    for enemy in enemies:
        while enemy.health > 0:
            hero.attack(enemy)
    
    items = hero.findItems()
    for item in items:
        while hero.distanceTo(item) > 2:
            hero.moveXY(item.pos.x, item.pos.y)
