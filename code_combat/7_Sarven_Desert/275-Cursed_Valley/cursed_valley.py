while True:
    enemy = hero.findNearestEnemy()
    if enemy and enemy.team == "ogres" and enemy.type == "skeleton":
        hero.attack(enemy)
    
    item = hero.findNearestItem()
    if item and item.type == "potion" and hero.health < hero.maxHealth / 4:
        hero.moveXY(item.pos.x, item.pos.y)
