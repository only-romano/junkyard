for x in range(12, 12 + 8 * 6, 8):
    for y in range(12, 12 + 8 * 7, 8):
        hero.buildXY("fire-trap", x, y)
    hero.moveXY(hero.pos.x + 8, hero.pos.y)

mine = hero.findNearest(hero.findHazards())

while True:
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) <= 20:
        hero.moveXY(mine.pos.x, mine.pos.y)
        break
