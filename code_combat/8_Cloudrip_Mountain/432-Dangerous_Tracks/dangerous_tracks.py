def buildFireTraps(start, end, step, x, y):
    for i in range(start, end+1, step):
        if x:
            hero.buildXY("fire-trap", x, i)
        else:
            hero.buildXY("fire-trap", i, y)


buildFireTraps(40, 112, 24, False, 114)
buildFireTraps(110, 38, -18, 140, False)
buildFireTraps(132, 32, -20, False, 22)
buildFireTraps(28, 108, 16, 20, False)
hero.moveXY(40, 94)
