def onSpawn(e):
    remainingPeasants = 3
    while remainingPeasants > 0:
        pet.moveXY(40, 55)
        peasant = pet.findNearestByType("peasant")
        if peasant:
            pet.carryUnit(peasant, 40, 34)
            remainingPeasants -= 1

    munchkin = pet.findNearestByType("munchkin")
    if munchkin:
        pet.carryUnit(munchkin, 41, 19)


pet.on("spawn", onSpawn);

while True:
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 10:
        hero.attack(enemy)
