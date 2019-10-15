def hitOrHide(target):
    if target:
        hero.attack(target)
        hero.moveXY(32, 16)

while True:
    enemy = hero.findNearestEnemy()
    hitOrHide(enemy)
