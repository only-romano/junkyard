def findSoldierOffset(soldiers, i):
    soldier = soldiers[i]
    angle = i * 360 / soldiers.length
    return radialToCartesian(5, angle)


def radialToCartesian(radius, degrees):
    radians = Math.PI / 180 * degrees
    xOffset = radius * Math.cos(radians)
    yOffset = radius * Math.sin(radians)
    return {x: xOffset, y: yOffset}


peasant = hero.findByType("peasant")[0]
while True:
    soldiers = hero.findByType("soldier")
    for i in range(len(soldiers)):
        offset = findSoldierOffset(soldiers, i)
        moveTo = {"x": peasant.pos.x + offset.x, "y": peasant.pos.y + offset.y}
        hero.command(soldiers[i], "move", moveTo)
    hero.move({x: hero.pos.x + 0.2, y: hero.pos.y})
