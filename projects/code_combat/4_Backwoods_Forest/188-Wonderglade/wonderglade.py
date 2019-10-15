while True:
    item = hero.findNearestItem();;
    if item and item.type != "gem":
        hero.moveXY(item.pos.x, item.pos.y)
