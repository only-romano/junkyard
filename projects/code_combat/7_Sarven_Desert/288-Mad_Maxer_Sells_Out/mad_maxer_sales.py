while True:
    closestGold = None
    minGoldDist = 9999
    coinIndex = 0
    coins = hero.findItems()
    while coinIndex < coins.length:
        gold = coins[coinIndex]
        coinIndex += 1
        if gold.value != 3:
            continue
        distance = hero.distanceTo(gold)
        if distance < minGoldDist:
            minGoldDist = distance
            closestGold = gold
    if closestGold:
        hero.moveXY(closestGold.pos.x, closestGold.pos.y)
