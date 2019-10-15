def chooseStrategy():
    enemies = hero.findEnemies()
    if enemies.length > 20:
        return "retreat"
    elif enemies.length > 0:
        return "attack"
    elif hero.built.length % 9 == 0:
        return "start-next-trap-column"
    else:
        return "build-next-trap-in-column"


trapsInColumn = 9
startX = 40
columnX = startX


def buildNextTrapInColumn(columnX,numTraps):
    newY = 7 * (numTraps % 9) + 10
    if hero.pos.y < newY:
        hero.move({"x": columnX - 5, "y": newY})
    else:
        buildTrap(columnX,newY)


def startNextTrapColumn(columnX, numTraps):
    newX = startX - (Math.floor(numTraps / trapsInColumn) * 6)
    if hero.pos.y > 10:
        hero.move({"x": newX - 5, "y": 10})
        return columnX
    else:
        buildTrap(newX,10)
        return newX


def buildTrap(x, y):
    hero.buildXY("fire-trap", x, y)


def commandAttack():
    friends = hero.findFriends()
    for friend in friends:
        enemy = friend.findNearestEnemy()
        if enemy:
            hero.command(friend, "attack", enemy)

def commandRetreat():
    hero.say("Retreat!")
    friends = hero.findFriends()
    for friend in friends
        hero.command(friend, "move", {x: 10, y: friend.pos.y})
    hero.moveXY(8, 42)


while True:
    strategy = chooseStrategy()
    if strategy == "attack":
        commandAttack()
    elif strategy == "build-next-trap-in-column":
        buildNextTrapInColumn(columnX, hero.built.length)
    elif strategy == "start-next-trap-column":
        columnX = startNextTrapColumn(columnX, hero.built.length)
    elif strategy == "retreat":
        commandRetreat()
