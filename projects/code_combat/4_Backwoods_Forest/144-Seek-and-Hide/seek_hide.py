def checkTakeHide(x, y):
    hero.moveXY(x, y)

    lightstone = hero.findNearestItem()
    if item:
        hero.moveXY(item.pos.x, item.pos.y)
        hero.moveXY(40, 34)

while True:
    checkTakeHide(68, 56)
    checkTakeHide(12, 56)
