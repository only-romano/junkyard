def maybeBuildTrap(x, y):
    hero.moveXY(x, y)
    if hero.findNearestEnemy():
        hero.buildXY("fire-trap", x, y)

while True:
    maybeBuildTrap(43, 50)
    maybeBuildTrap(25, 34)
    maybeBuildTrap(43, 20)
