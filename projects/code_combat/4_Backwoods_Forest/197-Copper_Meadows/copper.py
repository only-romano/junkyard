hero.cast("haste", hero)

while True:
    flag = hero.findFlag()
    if flag:
        if hero.isReady("jump"):
            hero.jumpTo(flag.pos)
        hero.pickUpFlag(flag)
        if hero.canCast("haste"):
            hero.cast("haste", hero)
        elif hero.isReady("reset-cooldown"):
            hero.resetCooldown("haste")
    else:
        item = hero.findNearestItem()
        if item:
            if hero.distanceTo(item) > 12 and hero.isReady("jump"):
                hero.jumpTo(item.pos)
            if hero.canCast("haste"):
                hero.cast("haste", hero)
            hero.moveXY(item.pos.x, item.pos.y)
