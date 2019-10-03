while True:
    flag = hero.findFlag()
    item = hero.findNearestItem()
    if flag:
        pos = flag.pos
        hero.pickUpFlag(flag);
        hero.buildXY("fire-trap", pos.x, pos.y)
    if item:
        hero.moveXY(item.pos.x, item.pos.y)
