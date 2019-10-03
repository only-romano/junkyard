def startsWith(phrase, word):
    if len(word) > len(phrase):
        return False
    for i in range(len(word)):
        if phrase[i] != word[i]:
            return False
    return True


def onHear(event):
    if startsWith(event.speaker.id, "Exp"):
        potion = pet.findNearestByType("potion")
        if potion:
            pet.fetch(potion)
            pet.moveXY(28, 34)


pet.on("hear", onHear)
while True:
    nearest = hero.findNearest(hero.findByType("mushroom"))
    if nearest:
        hero.moveXY(nearest.pos.x, nearest.pos.y)
