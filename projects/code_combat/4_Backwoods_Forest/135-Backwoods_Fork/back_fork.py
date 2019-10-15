def checkAndAttack(target):
    if target:
        hero.attack(target)
    hero.moveXY(43, 34)

while True:
    hero.moveXY(58, 52)
    checkAndAttack(hero.findNearestEnemy())

    hero.moveXY(58, 16)
    checkAndAttack(hero.findNearestEnemy())
