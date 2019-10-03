while True:
    item = hero.findNearestItem()
    distance = hero.distanceTo(item)
    if item.type == "gem" || hero.distanceTo(item) < 20:
        hero.moveXY(item.pos.x, item.pos.y)
