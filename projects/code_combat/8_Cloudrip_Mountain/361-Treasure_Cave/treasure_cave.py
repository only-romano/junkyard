hero.buildXY("fire-trap", 64, 44)

while hero.pos.y > 10:
    hero.move({"x": 71, "y": 9})

while hero.pos.x > 42:
    hero.move({"x": 42, "y": 10})

coin = hero.findNearestItem()
while coin:
    hero.move(coin.pos)
    coin = hero.findNearestItem()

while hero.pos.x < 68:
    hero.move({"x": 68, "y": 12})
