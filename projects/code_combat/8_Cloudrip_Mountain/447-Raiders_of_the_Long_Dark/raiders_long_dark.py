arryn = hero.findByType("raider")[0]
peasant = hero.findByType("peasant")[0]


def chooseHeroStrategy():
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) <= 5 and hero.distanceTo(peasant) < 15
        return "fight"
    return "advance"


def heroFight():
    enemy = hero.findNearestEnemy()
    if enemy:
        if hero.isReady("bash"):
            hero.bash(enemy)
        else:
            hero.attack(enemy)


def heroAdvance():
    hero.move({"x": peasant.pos.x - 5, "y": peasant.pos.y})


def choosePeasantStrategy():
    if hero.isPathClear(peasant, {"x": peasant.pos.x, "y": peasant.pos.y + 8}):
        return "build-above"
    if hero.isPathClear(peasant, {"x": peasant.pos.x, "y": peasant.pos.y - 8}):
        return "build-below"
    return "follow"


def peasantAdvance():
    hero.command(peasant, "move", {"x": arryn.pos.x - 5, "y": arryn.pos.y})


def peasantBuild(x,y):
    hero.command(peasant, "buildXY", "palisade", x, y)


while True:
    heroStrategy = chooseHeroStrategy()
    if heroStrategy == "fight":
        heroFight()
    elif heroStrategy == "advance":
        heroAdvance()
    
    peasantStrategy = choosePeasantStrategy()
    if peasantStrategy == "build-above":
        peasantBuild(peasant.pos.x, peasant.pos.y + 5)
    elif peasantStrategy == "build-below":
        peasantBuild(peasant.pos.x, peasant.pos.y - 5)
    elif peasantStrategy == "follow":
        peasantAdvance()
