def passagePosByNum(n):
    return {"x": 60, "y": n * 12 + 8}


def onHear(event):
    message = event.message
    trimmed = message.strip()
    hidden = len(message) - len(trimmed)
    pos = passagePosByNum(hidden)
    pet.moveXY(pos.x, pos.y)
    pet.moveXY(2, pos.y)


pet.on("hear", onHear)

while True:
    hero.move(pet.pos)
