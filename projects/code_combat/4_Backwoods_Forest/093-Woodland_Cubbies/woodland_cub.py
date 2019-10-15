# You need an Elemental codex 1+ to cast "Haste"

def attackIfExists(x, y):
    hero.moveXY(x, y)
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

hero.cast("haste", hero)

attackIfExists(19, 33)
attackIfExists(49, 51)
attackIfExists(58, 14)
