customer = hero.findNearest(hero.findFriends())
x1 = customer.leftBottom.x
y1 = customer.leftBottom.y
x2 = customer.rightTop.x
y2 = customer.rightTop.y
step = 4

for y in range(y2 - step, y1 - 1, -step):
    hero.buildXY("fence", x1, y)


for x in range(x1 + step, x2 + 1, step):
    hero.buildXY("fence", x, y1)

for y in range(y1 + step, y2 + 1, step):
    hero.buildXY("fence", x2, y)

for x in range(x2 - step, x1 - 1, -step):
    hero.buildXY("fence", x, y2)
