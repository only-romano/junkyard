def cleaveOrAttack(x, y):
    hero.moveXY(x, y)
    ogre = hero.findNearestEnemy()
    if ogre:
        if hero.isReady("cleave"):
            hero.cleave(ogre)
        else:
            hero.attack(ogre)



while True:
    cleaveOrAttack(35, 34)
    cleaveOrAttack(60, 31)
