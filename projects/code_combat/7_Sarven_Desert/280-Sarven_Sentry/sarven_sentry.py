while True:
    flagGreen = hero.findFlag("green")
    flagBlack = hero.findFlag("black")
    
    if flagGreen:
        pos = flagGreen.pos
        hero.buildXY("fence", pos.x, pos.y)
        hero.pickUpFlag(flagGreen)

    if flagBlack:
        pos = flagBlack.pos
        hero.buildXY("fire-trap", pos.x, pos.y)
        hero.pickUpFlag(flagBlack)
    
    hero.moveXY(43, 31)
