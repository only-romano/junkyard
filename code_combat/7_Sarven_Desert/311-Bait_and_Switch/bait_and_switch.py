def collectUntil(enoughGold):
    while hero.gold < enoughGold:
        item = hero.findNearestItem()
        if item:
            hero.moveXY(item.pos.x, item.pos.y)


collectUntil(25)
hero.buildXY("decoy", 40, 52)
hero.moveXY(20, 52)

collectUntil(50)
hero.buildXY("decoy", 68, 22)
hero.buildXY("decoy", 30, 20)
