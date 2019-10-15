def maybeBuildSomething(typeToBuild, x, y):
    hero.moveXY(x, y)
    if hero.findNearestEnemy():
        hero.buildXY(typeToBuild, x, y)

while True:
    maybeBuildSomething("fire-trap", 40, 20)
    maybeBuildSomething("fence", 26, 34)
    maybeBuildSomething("fire-trap", 40, 50)
    maybeBuildSomething("fence", 54, 34)
