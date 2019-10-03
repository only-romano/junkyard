while True:
    flag = hero.findFlag()
    if flag:
        if hero.isReady("jump"):
            hero.jumpTo(flag.pos)
        hero.pickUpFlag(flag)
