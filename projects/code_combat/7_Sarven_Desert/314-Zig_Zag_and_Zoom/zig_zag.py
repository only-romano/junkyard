def mod15(n):
    while n >= 15:
        n -= 15
    return n


def mod9(n):
    while n >= 9:
        n -= 9
    return n


while True:
    time = hero.time
    if time < 30:
        y = 10 + 3 * mod15(time)
    else:
        y = 20 + 3 * mod9(time)
    x = 10 + time
    hero.moveXY(x, y)
