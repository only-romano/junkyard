def drawCircle(x, y, size):
    angle = 0
    hero.toggleFlowers(False)
    while angle <= Math.PI * 2:
        newX = x + (size * Math.cos(angle))
        newY = y + (size * Math.sin(angle))
        hero.moveXY(newX, newY)
        hero.toggleFlowers(True)
        angle += 0.2


def drawSquare(x, y, size):
    hero.toggleFlowers(False)
    cornerOffset = size / 2
    hero.moveXY(x - cornerOffset, y - cornerOffset)
    hero.toggleFlowers(True)
    hero.moveXY(x + cornerOffset, y - cornerOffset)
    hero.moveXY(x + cornerOffset, y + cornerOffset)
    hero.moveXY(x - cornerOffset, y + cornerOffset)
    hero.moveXY(x - cornerOffset, y - cornerOffset)


def drawK(x, y, size):
    hero.toggleFlowers(False)
    var cornerOffset = size / 2
    hero.moveXY(x - cornerOffset, y + cornerOffset)
    hero.toggleFlowers(True)
    hero.moveXY(x - cornerOffset, y - cornerOffset)
    hero.moveXY(x - cornerOffset, y)
    hero.moveXY(x, y + cornerOffset)
    hero.moveXY(x - cornerOffset, y)
    hero.moveXY(x, y - cornerOffset)


redX = {"x": 28, "y": 36}
whiteX = {"x": 44, "y": 36}

hero.setFlowerColor("pink")
drawCircle(redX["x"], redX["y"], 10)
hero.setFlowerColor("purple")
drawSquare(whiteX["x"], whiteX["y"], 10)
hero.setFlowerColor("random")
drawK(35, 20, 10)
