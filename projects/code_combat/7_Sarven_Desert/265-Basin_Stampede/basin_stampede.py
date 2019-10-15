while True:
    enemy = hero.findNearestEnemy()
    x = hero.pos.x + 5
    y = 17
    if enemy:
        if enemy.pos.y > hero.pos.y:
            y -= 3
        elif enemy.pos.y < hero.pos.y:
            y += 3
    hero.moveXY(x, y)
