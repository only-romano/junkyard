fenceMap = hero.findNearest(hero.findFriends()).getMap()


def convertCoor(row, col):
    return {"x": 34 + col * 4, "y": 26 + row * 4}



for i in range(len(fenceMap)):
    for j in range(len(fenceMap[i])):
        if fenceMap[i][j] == 1:
            pos = convertCoor(i, j)
            hero.buildXY("fence", pos["x"], pos["y"])

hero.moveXY(30, 18)
