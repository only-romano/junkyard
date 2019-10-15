def bestCoin(coins):
    bestValue = 0
    best = None
    for coin in coins:
        profit = coin.value / hero.distanceTo(coin)
        if profit > bestValue:
            bestValue = profit
            best = coin

    return best


coin = bestCoin(hero.findItems())
while hero.time < 20 and coin:
    hero.move(coin.pos)
    coin = bestCoin(hero.findItems())

while hero.pos.x > 16:
    hero.move({"x": 16, "y": 38})

hero.buildXY("fence", 21, 37)
