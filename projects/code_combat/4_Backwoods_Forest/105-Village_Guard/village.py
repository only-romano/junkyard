def patrol(x, y):
    hero.moveXY(x, y)
    enemy = hero.findNearestEnemy()
    if enemy:
        while enemy.health > 0:
            hero.attack(enemy)


while True:
    patrol(35, 34)
    patrol(60, 34)
