while True:
    flag = hero.findFlag()
    if flag:
        hero.throwPos(flag.pos)
        hero.removeFlag(flag)
