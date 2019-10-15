def onSpawn(e):
    while True:
        enemy = pet.findNearestByType("munchkin")
        if enemy && pet.isReady("chase"):
            pet.chase(enemy)
        potion = pet.findNearestByType("potion")
        if potion:
            pet.fetch(potion)

pet.on("spawn", onSpawn)
