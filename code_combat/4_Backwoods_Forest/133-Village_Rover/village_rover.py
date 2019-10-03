def findAndAttackEnemy(x, y):
    hero.moveXY(x, y)
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

while True:
    findAndAttackEnemy(35, 34)
    findAndAttackEnemy(60, 31)
