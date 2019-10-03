from math import pi

def degreesToRadians(degrees):
    return pi / 180 * degrees
    

def line(start, end):
    full = Vector.subtract(end, start)
    distance = full.magnitude()
    if distance < 4:
        hero.toggleFlowers(False)
        hero.moveXY(start.x, start.y)
        hero.toggleFlowers(True)
        hero.moveXY(end.x, end.y)
        return
    
    half = Vector.divide(full, 2)
    A = Vector.add(half, start)

    rotate = Vector.rotate(half, degreesToRadians(90))
    rotate = Vector.multiply(rotate, 2 / 3)
    B = Vector.add(rotate, A)

    line(start, A)
    line(A, B)
    line(B, A)
    line(A, end)


def flake (start, end):
    side = Vector.subtract(end, start)
    a = start
    b = end
    for i in range(6):
        line(a, b)
        side = Vector.rotate(side, degreesToRadians(60))
        a = b
        b = Vector.add(side, a)


whiteXs = [Vector(12, 10), Vector(60, 10)]
redXs = [Vector(64, 52), Vector(52, 52)]

flake(redXs[0], redXs[1])
line(whiteXs[0], whiteXs[1])
