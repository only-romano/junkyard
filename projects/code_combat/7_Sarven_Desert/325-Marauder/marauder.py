while True:
    coin = hero.findNearestItem()
    while coin:
        hero.moveXY(coin.pos.x, coin.pos.y)
        coin = hero.findNearestItem()

    enemy = hero.findNearestEnemy()
    if enemy:
        while enemy.health > 0:
            if hero.isReady("bash"):
                hero.bash(enemy)
            else:
                hero.attack(enemy)
