while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        isLeft = hero.pos.x  > enemy.pos.x
        isAbove = hero.pos.y < enemy.pos.y
        isRight = enemy.pos.x > hero.pos.x
        isBelow = enemy.pos.y < hero.pos.y

        if isLeft and isAbove:
            hero.buildXY("fire-trap", 20, 51)
        if isAbove and isRight:
            hero.buildXY("fire-trap", 60, 51)
        if isAbove and isLeft:
            hero.buildXY("fire-trap", 20, 51)
        if isBelow and isLeft:
            hero.buildXY("fire-trap", 20, 17)
        if isBelow && isRight:
            hero.buildXY("fire-trap", 60, 17)
        
        hero.moveXY(40, 34)
    else:
        hero.moveXY(40, 34)
