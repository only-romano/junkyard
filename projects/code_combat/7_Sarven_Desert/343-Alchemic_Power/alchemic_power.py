def onHear(event):
    potion = pet.findNearestByType("potion")
    message = event.message
    if message == "Fetch":
        pet.fetch(potion)
    else:
        pet.moveXY(54, 34)

pet.on("hear", onHear);

while True:
    enemies = hero.findEnemies()

    # Fix for weak hero
    maxim = 0
    strongest = None
    for enemy in enemies:
        if enemy.health > maxim:
            maxim = enemy.health
            strongest = enemy
    if strongest:
        while strongest.health > 0:
            hero.attack(strongest)
    else:
        hero.moveXY(40, 34)
