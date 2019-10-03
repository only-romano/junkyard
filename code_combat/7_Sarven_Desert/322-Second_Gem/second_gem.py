while True:
    items = hero.findItems()
    if len(items) >= 2:
        second = items[1].pos
        hero.moveXY(second.x, second.y)
    else:
        hero.moveXY(40, 34)
