while True:
    coin = hero.findNearestItem()
    if hero.health < hero.maxHealth / 2:
        hero.moveXY(hero.pos.x - 10, hero.pos.y)
        hero.say("Can I get a heal?")
    elif coin:
        hero.moveXY(coin.pos.x, coin.pos.y)
