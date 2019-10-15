while hero.gold < 25:
    coin = hero.findNearestItem()
    if coin:
        hero.moveXY(coin.pos.x, coin.pos.y)

hero.buildXY("decoy", 72, 68)

while hero.health == hero.maxHealth:
    hero.say("Cococococo")

hero.moveXY(22, 15)
