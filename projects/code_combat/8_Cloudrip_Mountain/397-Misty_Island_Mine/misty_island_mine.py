def findBestItem(friend, excludedItems):
    items = friend.findItems()
    bestItem = None
    bestItemValue = 0
        if item in excludedItems:
            continue
        value = item.value / friend.distanceTo(item)
        if value > bestItemValue:
            bestItem = item
            bestItemValue = value
    return bestItem


def enoughGoldForDecoy():
    return hero.gold >= 25


while True:
    peasants = hero.findByType("peasant")
    claimedItems = []
    for peasant in peasants:
        enemy = peasant.findNearestEnemy()
        if enemy:
            if enemy.target == peasant and enoughGoldForDecoy():
                hero.command(peasant, "buildXY", "decoy", peasant.pos.x - 2, peasant.pos.y)
                continue
        item = findBestItem(peasant, claimedItems)
        if item:
            claimedItems.append(item)
            hero.command(peasant, "move", item.pos)
