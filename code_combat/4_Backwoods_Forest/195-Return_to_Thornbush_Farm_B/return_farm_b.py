def maybeBuildTrap(x, y):
    hero.moveXY(x, y)
    if hero.findNearestEnemy():
        hero.buildXY("fire-trap", x, y)

while True:
    maybeBuildTrap(38, 20)
    maybeBuildTrap(56, 34)
    maybeBuildTrap(38, 48)
