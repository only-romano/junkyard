def ambushAttack(target):
    if target:
        hero.attack(target)
        hero.moveXY(52, 36)

while True:
    ogre = hero.findNearestEnemy()
    ambushAttack(ogre)
