yak = hero.findNearestEnemy()

while yak:
    item = hero.findNearestItem()
    if item:
        hero.moveXY(item.pos.x, item.pos.y)
    yak = hero.findNearestEnemy()

hero.moveXY(38, 58)
