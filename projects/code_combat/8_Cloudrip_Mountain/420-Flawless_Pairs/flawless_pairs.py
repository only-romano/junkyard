def findValuePair(items):
    for i in range(len(items)):
        itemI = items[i]
        for j in range(len(items)):
            if i == j:
                continue
            itemJ = items[j]
            if itemI.value == itemJ.value:
                return [itemI, itemJ]
    return None


while True:
    gems = hero.findItems()
    gemPair = findValuePair(gems)
    if gemPair:
        gemA = gemPair[0]
        gemB = gemPair[1]
        hero.moveXY(gemA.pos.x, gemA.pos.y)
        hero.moveXY(40, 44)
        hero.moveXY(gemB.pos.x, gemB.pos.y)
        hero.moveXY(40, 44)
