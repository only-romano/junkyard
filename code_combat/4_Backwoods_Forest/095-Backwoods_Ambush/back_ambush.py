# You need an Elemental codex 1+ to cast "Haste"

def attackIfExists(x, y):
    hero.moveXY(x, y)
    enemy = hero.findNearestEnemy()
    if enemy:
        while enemy.health > 0:
            hero.attack(enemy)

hero.cast("haste", hero)

attackIfExists(24, 42)
attackIfExists(27, 60)
attackIfExists(42, 50)
attackIfExists(39, 24)
