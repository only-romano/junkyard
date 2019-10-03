def square(startX, endX, startY, endY, unit):
    for x in range(startX, endX, 8):
        for y in range(startY, endY, 8):
            hero.summon(unit)
            hero.command(hero.built[-1], "move", {"x": x, "y": y})


sergeant = hero.findNearest(hero.findByType("soldier"))
width = sergeant.rectWidth
height = sergeant.rectHeight

square(8, 9 + width, 8, 9 + height, "soldier")

sniper = hero.findNearest(hero.findByType("archer"))
archerX2 = sniper.archerX2
archerY2 = sniper.archerY2

square(48, 1 + archerX2, 8, 1 + archerY2, "archer")
