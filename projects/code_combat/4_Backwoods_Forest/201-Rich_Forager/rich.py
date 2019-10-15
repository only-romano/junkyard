while True:
    flag = hero.findFlag()
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()

    if flag:
        if hero.isReady("jump"):
            hero.jumpTo(flag.pos)
        hero.pickUpFlag(flag)
    elif enemy:
        if hero.canCast("chain-lightning"):
            hero.cast("chain-lightning", enemy)
        elif hero.distanceTo(enemy) < 15:
            hero.cast("drain-life", enemy)
        else:
            hero.attack(enemy)
    elif item:
        if item.type != "poison":
            if hero.isReady("jump"):
                hero.jumpTo(item.pos)
            hero.moveXY(item.pos.x, item.pos.y);
