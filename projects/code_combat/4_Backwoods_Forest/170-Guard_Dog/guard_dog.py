def onSpawn(event):
    while True:
        if pet.findNearestEnemy():
            pet.say("Ahoy!")

pet.on("spawn", onSpawn)
