def isCoinClose(coin):
    return hero.distanceTo(coin) < 20

while True:
    item = hero.findNearestItem()
    if item and isCoinClose(item):
        hero.moveXY(item.pos.x, item.pos.y)
