pos = {x: hero.pos.x, y: hero.pos.y}

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.buildXY("fire-trap", enemy.pos.x - 20, enemy.pos.y)
    pos.y = pos.y - 10
    hero.moveXY(pos.x, pos.y)
