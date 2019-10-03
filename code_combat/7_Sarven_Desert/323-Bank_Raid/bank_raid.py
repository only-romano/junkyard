while True:
    enemies = hero.findEnemies()
    for enemy in enemies:
        if enemy.health > 0:
            hero.attack(enemy)

    coins = hero.findItems()
    for coin in coins:
        hero.moveXY(coin.pos.x, coin.pos.y)
