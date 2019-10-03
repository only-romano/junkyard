def onHear(event):
    if event.speaker == hero:
        pet.say("WOOF")


pet.on("hear", onHear)

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.say("Ahoy!")
        hero.moveXY(30, 33)
        hero.moveXY(30, 14)
