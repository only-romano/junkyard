def findMostHealth(enemies):
    target = None
    targetHealth = 0
    for enemy in enemies:
        if enemy.health > targetHealth:
            target = enemy
            targetHealth = enemy.health

    return target


def valueOverDistance(item):
    return item.value / hero.distanceTo(item)


def findBestItem(items):
    bestItem = None
    bestValue = 0
    
    for item in items:
        value = valueOverDistance(item)
        if value > bestValue:
            bestValue = value
            bestItem = item

    return bestItem


while True:
    enemy = findMostHealth(hero.findEnemies())

    if enemy and enemy.health > 15:
        while enemy.health > 0:
            hero.attack(enemy)
    else:
        coin = findBestItem(hero.findItems())
        if coin:
            hero.moveXY(coin.pos.x, coin.pos.y)
