def onSpawn():
    while True:
        pet.moveXY(48, 8)
        pet.moveXY(12, 8)

pet.on("spawn", onSpawn)
while True:
    hero.say("Run!!!")
    hero.say("Faster!")
