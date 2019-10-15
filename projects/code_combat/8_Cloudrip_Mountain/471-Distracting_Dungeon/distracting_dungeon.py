def moveBothTo(point):
    while hero.distanceTo(point) > 1:
        hero.move(point)
        hero.command(peasant, "move", point)


peasant = hero.findNearest(hero.findFriends())

while True:
    hero.command(peasant, "buildXY", "decoy", peasant.pos.x + 2, peasant.pos.y)
    var nextPoint = {"x": hero.pos.x, "y": hero.pos.y + 28}
    moveBothTo(nextPoint)
    nextPoint = {"x": hero.pos.x + 28, "y": hero.pos.y}
    var enemy = hero.findNearestEnemy()
    while enemy:
        while enemy.health > 0:
            hero.attack(enemy)
        enemy = hero.findNearestEnemy()
    moveBothTo(nextPoint)
