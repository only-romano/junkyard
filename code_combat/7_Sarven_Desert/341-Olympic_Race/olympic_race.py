def onHear(event){
    referee = pet.findNearestByType("wizard")
    if event.speaker == referee and event.message == "Start":
        pet.moveXY(54, 27)
        pet.moveXY(6, 27)


pet.on("hear", onHear)
