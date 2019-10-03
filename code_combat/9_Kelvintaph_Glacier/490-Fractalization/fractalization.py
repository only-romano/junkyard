def degreesToRadians(degrees):
    return Math.PI / 180 * degrees


def koch(start, end):
    full = Vector.subtract(end, start)
    distance = full.magnitude()
    if distance < 3:
        hero.toggleFlowers(False)
        hero.moveXY(start.x, start.y)
        hero.toggleFlowers(True)
        hero.moveXY(end.x, end.y)
        return
    third = Vector.multiply(full, 1 / 3)
    A = Vector.add(start, third)
    B = Vector.add(A, Vector.rotate(third, degreesToRadians(60)))
    C = Vector.add(A, third)
    koch(start, A)
    koch(A, B)
    koch(B, C)
    koch(C, end)


whiteXs = [Vector(6, 6), Vector(74, 6), Vector(74, 61), Vector(6, 61)]
koch(whiteXs[0], whiteXs[1])
koch(whiteXs[1], whiteXs[2])
koch(whiteXs[2], whiteXs[3])
koch(whiteXs[3], whiteXs[0])
