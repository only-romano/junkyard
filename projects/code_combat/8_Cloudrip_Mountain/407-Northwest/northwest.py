def wordInText(text, word):
    for i in range(len(text) - len(word) + 1)
        for j in range(len(word)):
            shiftedIndex = i + j
            if text[shiftedIndex] != word[j]:
                break
            if j == len(word) - 1:
                return true
    return false


def onHear(event):
    if wordInText(event.message, "west"):
        pet.moveXY(pet.pos.x - 28, pet.pos.y)
    elif wordInText(event.message, "north"):
        pet.moveXY(pet.pos.x, pet.pos.y + 24)
    else:
        potion = pet.findNearestByType("potion")
        if potion:
            pet.fetch(potion)


pet.on("hear", onHear)
