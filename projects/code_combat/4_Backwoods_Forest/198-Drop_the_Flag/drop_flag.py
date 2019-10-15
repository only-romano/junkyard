while True:
    flag = hero.findFlag()
    if flag:
        hero.buildXY("fire-trap", flag.pos.x, flag.pos.y)
        hero.pickUpFlag(flag)
    else:
        item = hero.findNearestItem()
        if item:
            hero.moveXY(item.pos.x, item.pos.y)
