while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        if enemy.pos.x < hero.pos.x:
            hero.buildXY("fire-trap", 25, 34)
        elif enemy.pos.x > hero.pos.x:
            hero.buildXY("fire-trap", 55, 34)
        elif enemy.pos.y < hero.pos.y:
            hero.buildXY("fire-trap", 40, 19)
        elif enemy.pos.y > hero.pos.y:
            hero.buildXY("fire-trap", 40, 49)
    hero.moveXY(40, 34)
