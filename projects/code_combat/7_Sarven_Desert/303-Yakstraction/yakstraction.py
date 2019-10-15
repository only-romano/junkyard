def flagFunc(flag):
    pos = flag.pos
    if hero.gold >= 25:
        hero.buildXY("decoy", pos.x, pos.y)
    hero.pickUpFlag(flag)


while True:
    flag = hero.findFlag()
    if flag:
        flagFunc(flag)
    item = hero.findNearestItem()
    if item:
        hero.moveXY(item.pos.x, item.pos.y)
