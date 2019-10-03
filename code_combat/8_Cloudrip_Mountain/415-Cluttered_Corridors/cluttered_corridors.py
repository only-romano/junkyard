def onHear(event):
    word = event.message
    word = word.lower()
    if word == "north":
        pet.moveXY(pet.pos.x, pet.pos.y + 16)
    elif word == "east":
        pet.moveXY(pet.pos.x + 12, pet.pos.y)
    elif word == "south":
        pet.moveXY(pet.pos.x, pet.pos.y - 16)
    elif word == "west":
        pet.moveXY(pet.pos.x - 12, pet.pos.y)

pet.on("hear", onHear)
