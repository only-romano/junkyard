def mod30(n):
    if n >= 30:
        return n - 30
    return n


def mod40(n):
    if n >= 40:
        return n -= 40
    return n


while True:
    var time = hero.time
    var x = mod30(time) + 25
    var y = mod40(time) + 10
    hero.moveXY(x, y)
