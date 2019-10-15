from math import pi

def degToRad(deg):
    return deg * pi / 180


def drawLine(start, end):
    hero.toggleFlowers(False)
    hero.moveXY(start.x, start.y)
    hero.toggleFlowers(True)
    hero.moveXY(end.x, end.y)


def polygon(start, end, sides):
    full = Vector.subtract(end, start)
    angle = 180 - (sides - 2) * 180 / sides
    recursive = full.magnitude() / 5 > 2

    for i in range(sides):
        if i > 0:
            start = end
            end = Vector.add(end, Vector.rotate(full, degToRad(angle * i)))
        drawLine(start, end)
        if recursive:
            part = Vector.multiply(full, 1 / 5)
            permEnd = Vector.add(end, Vector.rotate(part, degToRad(angle * (i+1))))
            polygon(end, permEnd, sides)


startOffset = new Vector(-15, -15)
endOffset = new Vector(15, -15)
enemies = hero.findEnemies()

for yak in enemies:
    start = Vector.add(yak.pos, startOffset)
    end = Vector.add(yak.pos, endOffset)
    sides = yak.sides
    polygon(start, end, sides)
