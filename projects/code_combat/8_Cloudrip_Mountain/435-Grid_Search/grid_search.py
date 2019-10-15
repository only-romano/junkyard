leftBorder = 20
rightBorder = 61
bottomBorder = 20
topBorder = 51
step = 10

for x in range(leftBorder, rightBorder, step):
    for y in range(bottomBorder, topBorder, step):
        hero.moveXY(x, y)
        hero.say("Anything")

hero.moveXY(20, 10)
