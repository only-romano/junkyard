while True:
    x = hero.pos.x
    y = hero.pos.y
    yak = hero.findNearestEnemy()

    if hero.distanceTo(yak) < 10:
        x += 10;
        hero.moveXY(x, y)
