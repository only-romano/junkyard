def onSpawn(event):
    while(true) {
        item = hero.findNearestItem()
        if item:
            pet.fetch(item)

pet.on("spawn", onSpawn)
hero.moveXY(78, 35)
