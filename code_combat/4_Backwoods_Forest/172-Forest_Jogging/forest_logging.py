def onSpawn(event):
    while True
        pet.moveXY(9, 24)
        pet.moveXY(30, 43)
        pet.moveXY(51, 24)
        pet.moveXY(30, 5)


def castIt():
    if hero.canCast("haste"):
        hero.cast("haste", pet)
    elif hero.isReady("reset-cooldown"):
        hero.resetCooldown("haste")

pet.on("spawn", onSpawn);


while True
    castIt()
    hero.say("Good dog!");
    hero.say("You can do it!");
    castIt()
    hero.say("Run Run Run!");
    hero.say("Almost!");
    castIt()
    hero.say("One more lap!");
