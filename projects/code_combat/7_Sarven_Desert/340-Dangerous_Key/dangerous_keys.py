def onHear(event):
    paladinUnit = pet.findNearestByType("paladin")
    goldKey = pet.findNearestByType("gold-key")
    silverKey = pet.findNearestByType("silver-key")
    bronzeKey = pet.findNearestByType("bronze-key")
    message = event.message;
    if event.speaker == paladinUnit:
        if message == "Gold":
            pet.fetch(goldKey)
        elif message == "Silver":
            pet.fetch(silverKey)
        elif message == "Bronze":
            pet.fetch(bronzeKey)


pet.on("hear", onHear)
