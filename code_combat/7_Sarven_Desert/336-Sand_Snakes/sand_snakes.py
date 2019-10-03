while True:
    coins = hero.findItems()
    nearest = None
    nearestDistance = 9999
    for coin in coins:
        distance = hero.distanceTo(coin)
        if distance < nearestDistance:
            nearest = coin
            nearestDistance = distance
    if nearest:
        hero.moveXY(nearest.pos.x, nearest.pos.y)
