def primeCheck(number):
    end = number ** 0.5
    for i in range(2, end):
        if number % i == 0:
            return False
    return True


def passMines(mines):
    for mine in mines:
        if primeCheck(mine.value):
            return mine


def getWay(mine, direction):
    way = []
    if direction == "west":
        way.append({"x": mine.pos.x + 7, "y": mine.pos.y})
        way.append({"x": mine.pos.x - 7, "y": mine.pos.y})
    elif direction == "east":
        way.append({"x": mine.pos.x - 7, "y": mine.pos.y})
        way.append({"x": mine.pos.x + 7, "y": mine.pos.y})
    elif direction == "north":
        way.append({"x": mine.pos.x, "y": mine.pos.y - 7})
        way.append({"x": mine.pos.x, "y": mine.pos.y + 7})
    return way


def findMines(x1, x2, y1, y2):
    mines = hero.findHazards()
    result = []
    for mine in mines:
        pos = mine.pos
        if pos.x > x1 and pos.x < x2 and pos.y > y1 and pos.y < y2:
            result.append(mine)
    return result


def moveTheWay(x1, x2, y1, y2, direction):
    mines = findMines(x1, x2, y1, y2)
    mine = passMines(mines)
    if mine:
        way = getWay(mine, direction)
        hero.moveXY(way[0]["x"], way[0]["y"])
        hero.moveXY(way[1]["x"], way[1]["y"])
        return way


def commandUnits(way, friends):
    moveUnits(way[0], friends)
    moveUnits(way[1], friends)


def moveUnits(pos, friends):
    for friend in friends:
        hero.command(friend, "move", pos)
    hero.wait(1.5)


friends = hero.findFriends()
commandUnits(moveTheWay(56, 63, 25, 50, "west"), friends)
commandUnits(moveTheWay(33, 45, 25, 50, "west"), friends)
commandUnits(moveTheWay(14, 24, 25, 50, "west"), friends)
moveUnits({"x": 5, "y": 10}, friends)
hero.moveXY(5, 10)
commandUnits(moveTheWay(5, 15, 0, 20, "east"), friends)
commandUnits(moveTheWay(25, 35, 0, 20, "east"), friends)
commandUnits(moveTheWay(45, 55, 0, 20, "east"), friends)
commandUnits(moveTheWay(65, 75, 0, 20, "east"), friends)
moveUnits({"x": 90, "y": 10}, friends)
hero.moveXY(90, 10)
commandUnits(moveTheWay(80, 105, 10, 25, "north"), friends)
commandUnits(moveTheWay(80, 105, 25, 40, "north"), friends)
commandUnits(moveTheWay(80, 105, 40, 55, "north"), friends)
