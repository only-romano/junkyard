while True:
    bestCoin = None
    maxRating = 0
    coinIndex = 0
    coins = hero.findItems()
    while coinIndex < coins.length:
        gold = coins[coinIndex]
        coinIndex += 1
        rating = gold.value / hero.distanceTo(gold)
        if rating > maxRating and gold.pos.x < 40:
            maxRating = rating
            bestCoin = gold

    if bestCoin:
        hero.moveXY(bestCoin.pos.x, bestCoin.pos.y)
