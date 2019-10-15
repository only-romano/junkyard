hero.moveXY(30, 25)

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.manaBlast()
