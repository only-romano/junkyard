def almostEqual(n1, n2):
    return abs(n1 - n2) <= 0.5


def allSameDistance(thangs):
    if len(thangs) == 0:
        return True
    etalon = hero.distanceTo(thangs[0])
    for thang in thangs:
        if not almostEqual(hero.distanceTo(thang), etalon):
            return False
    return True


bombs = hero.findEnemies()
for x in range(36, 44):
    for y in range(30, 39):
        hero.moveXY(x, y)
        if allSameDistance(bombs):
            hero.say("HEEEEEEEEEY!!!")
            hero.moveXY(40, 56)

hero.say("Heh. Nothing.")
