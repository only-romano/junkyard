while True:
    evilstone = hero.findNearestItem()
    if evilstone:
        x = evilstone.pos.x
        if x == 34:
            hero.moveXY(46, 22)
        else:
            hero.moveXY(34, 22)
    else:
        hero.moveXY(40, 22)
