while True:
    coins = hero.findItems()

    for coin in coins:
        if coin.value == 3:
            hero.moveXY(coin.pos.x, coin.pos.y)
