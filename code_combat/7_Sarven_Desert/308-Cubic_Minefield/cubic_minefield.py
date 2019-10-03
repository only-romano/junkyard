def mult(number, times):
    total = 0
    while times > 0:
        total += number
        times -= 1
    return total


def power(number, exponent):
    total = 1
    while exponent:
        total *= number
        exponent -= 1
    return total

tower = hero.findFriends()[0]
a = tower.a
b = tower.b
c = tower.c
d = tower.d
x = hero.pos.x

while True:
    y = a * power(x, 3) + b * power(x, 2) + c * power(x, 1) + d * power(x, 0)
    hero.moveXY(x, y)
    x = x + 5
