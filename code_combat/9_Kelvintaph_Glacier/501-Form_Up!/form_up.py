def markPos(i):
    return {"x": 12 + i * 8, "y": 12}


def findUnplacedSoldiers():
    friends = hero.findFriends()
    result = []
    for friend in friends:
        if friend.pos.y < 30 and friend.pos.y > 18 and friend.action == "idle":
            result.append(friend)
    return result


def minHealthUnit(units):
    smallest = None
    lessHealth = 99999
    for unit in units:
        if unit.health < lessHealth:
            smallest = unit
            lessHealth = unit.health
    return smallest


recruits = findUnplacedSoldiers()
markIndex = 0

while len(recruits):
    smallest = minHealthUnit(recruits)
    if smallest:
        hero.command(smallest, "move", markPos(markIndex))
    markIndex += 1
    recruits = findUnplacedSoldiers()
