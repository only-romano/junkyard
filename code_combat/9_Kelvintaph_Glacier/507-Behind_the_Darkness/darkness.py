def waitForAndAttack(abilityName):
    while True:
        if hero.isReady(abilityName):
            break
        enemy = hero.findNearestEnemy()
        if enemy and enemy.type != "yeti" and hero.distanceTo(enemy) < 15:
            hero.attack(enemy)


SE = {"x": 52, "y": 20}
NE = {"x": 52, "y": 48}
NW = {"x": 28, "y": 48}
SW = {"x": 28, "y": 20}
hero.wallOfDarkness([SW, NW, NE, SE])
waitForAndAttack("wall-of-darkness")
hero.wallOfDarkness([NE, SE, SW])
waitForAndAttack("wall-of-darkness")
hero.wallOfDarkness([NE, NW, SW])
waitForAndAttack("wall-of-darkness")
