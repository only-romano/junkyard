def goFetch():
    while True:
        potion = hero.findNearestItem()
        if potion:
            pet.fetch(potion)

pet.on("spawn", goFetch);

while True:
    if hero.canCast("haste"):
        hero.cast("haste", pet)
    elif hero.isReady("reset-cooldown"):
        hero.resetCooldown("haste")
