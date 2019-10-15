def patrol(x, y):
    hero.moveXY(x, y)
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.buildXY("fire-trap", x, y);


while True:
    patrol(43, 50)
    patrol(25, 34)
    patrol(43, 20)
