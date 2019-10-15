def commandIt(start, end, step, x, y):
    for i in range(start, end+1, step):
        if x:
            hero.moveXY(x, i)
        else:
            hero.moveXY(i, y)
        hero.say("Here")

commandIt(40, 80, 20, False, 60)
commandIt(40, 20, -20, 80, False)
commandIt(60, 20, -20, False, 20)
commandIt(40, 60, 20, 20, False)
hero.moveXY(50, 40)
