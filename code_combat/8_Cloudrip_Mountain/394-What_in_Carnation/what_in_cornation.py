from math import pi, sin, cos, copysign

twoPi = 2 * pi


def degreesToRadians(degrees):
    return (degrees/360)*twoPi


def drawPolyStars(center, radius, sides, skips, startAngle):
    hero.toggleFlowers(False)
    angle = startAngle
    x = center.x
    y = center.y
    hoops = skips + 1
    stepAngle = hoops * (twoPi / sides)
    if skips != 0 and sides % hoops == 0:
        hoops = skips
    endAngle = (twoPi * hoops) + startAngle
    while angle <= endAngle:
        var newX = x + radius * cos(angle)
        var newY = y + radius * sin(angle)
        hero.moveXY(newX, newY)
        hero.toggleFlowers(True)
        angle += stepAngle


def drawStar(center, radius, sides, skips, startAngle):
    skipsPlusOne = skips + 1
    if (sides/skipsPlusOne) != 1 and (sides % skipsPlusOne) == 0:
        index = skips
        while index >= 0:
            angle = startAngle + index * (twoPi / sides)
            drawPolyStars(center, radius, sides, skips, angle)
            index -= 1
    else:
        drawPolyStars(center, radius, sides, skips, startAngle)


def drawPolygon(center, radius, sides, startAngle):
    drawPolyStars(center, radius, sides, 0, startAngle)


def drawSpokes(center, radius, sides, startAngle):
    x = center.x
    y = center.y
    endAngle = twoPi + startAngle
    stepAngle = twoPi / sides
    angle = startAngle
    while angle < endAngle:
        newX = x + radius * cos(angle)
        newY = y + radius * sin(angle)
        if (hero.pos.x|0) == (x|0) or (hero.pos.y|0) == (y|0):
            hero.toggleFlowers(True)
            hero.moveXY(newX, newY)
        else:
            hero.toggleFlowers(False)
            hero.moveXY(newX, newY)
            hero.toggleFlowers(True)
            hero.moveXY(x, y)
        hero.toggleFlowers(False)
        angle += stepAngle


def getResult(loopNum, angle, endAngle):
    if loopNum < 0:
        return angle >= endAngle
    return angle <= endAngle


def drawSpiral(center, size, loopNum, startAngle):
    newX, x = center.x
    newY, y = center.y
    hero.toggleFlowers(False)
    hero.moveXY(x, y)
    hero.toggleFlowers(True)
    steps = size * 2
    direction = copysign(1, loopNum);
    stepAngle = twoPi / steps / direction
    loops = direction * loopNum
    stepSize = size / steps / loops
    curSize = 0
    angle = startAngle
    endAngle = (twoPi * loopNum) + startAngle

    while getResult(loopNum, angle, endAngle):
        newX = x + curSize * cos(angle)
        newY = y + curSize * sin(angle)
        hero.moveXY(newX, newY)
        angle += stepAngle
        curSize += stepSize
    newX = x + size * cos(endAngle)
    newY = y + size * sin(endAngle)
    hero.moveXY(newX, newY)


redX = {x: 28, y: 36};
whiteX = {x: 60, y: 36}

hero.setFlowerColor("red")
drawPolygon(redX, 10, 6, twoPi / 4)
drawSpokes(redX, 10, 3, twoPi / 4 * 3)

hero.setFlowerColor("white")
drawStar(whiteX, 6, 7, 2, twoPi / 4)
hero.setFlowerColor("pink")
drawSpiral({x: 60, y: 42}, 15,  1, twoPi / 4 * 3)
drawSpiral({x: 60, y: 42}, 15,  -1, twoPi / 4 * 3)
