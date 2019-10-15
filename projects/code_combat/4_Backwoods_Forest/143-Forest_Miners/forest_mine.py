def checkEnemyOrSafe(x, y):
    hero.moveXY(x, y)
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(target)
    else:
        hero.say("Here")

while True:
    checkEnemyOrSafe(64, 54)
    checkEnemyOrSafe(15, 14)
