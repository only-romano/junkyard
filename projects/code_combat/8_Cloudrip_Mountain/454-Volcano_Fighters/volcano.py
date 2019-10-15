def findMostLeft (units):
    if units.length == 0:
        return None
    mostLeft = units[0]
    for unit in units:
        if unit.pos.x < mostLeft.pos.x:
            mostLeft = unit
    return mostLeft


def findMostBottom (units):
    if units.length == 0:
        return None
    mostBottom = units[0]
    for unit in units:
        if unit.pos.y < mostBottom.pos.y:
            mostBottom = unit
    return mostBottom


paladins = hero.findByType("paladin")
topLeft = findMostLeft(paladins)
bottomRight = findMostBottom(paladins)

x = topLeft.pos.x
y = bottomRight.pos.y
hero.moveXY(x, y)

while True:
    hero.shield()
