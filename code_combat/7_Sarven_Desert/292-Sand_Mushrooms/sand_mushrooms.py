def onSpawn(event):
    while True:
        potion = pet.findNearestByType("potion")
        pet.fetch(potion)


pet.on("spawn", onSpawn)

while True:
    item = hero.findNearestItem()
    if item && hero.health > hero.maxHealth / 3:
        hero.move(item.pos)
