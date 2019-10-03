while True:
    x = hero.pos.x
    y = hero.pos.y

    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 10:
        x -= 10
    else:
        x += 10

    hero.moveXY(x, y)
