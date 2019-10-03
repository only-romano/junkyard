def onSpawn():
    while True:
        scout = pet.findNearestByType("scout")
        if scout and pet.isReady("charm"):
            pet.charm(scout)


pet.on("spawn", onSpawn)
while True:
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 10:
        hero.attack(enemy)
    else:
        hero.moveXY(15, 42)
