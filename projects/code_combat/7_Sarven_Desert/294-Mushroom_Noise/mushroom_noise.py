def onSpawn(event):
    potion = pet.findNearestByType("potion")
    if potion:
        pet.fetch(potion)
    goldKey = pet.findNearestByType("gold-key")
    if goldKey:
        pet.fetch(goldKey)


skeleton = pet.findNearestByType("skeleton")
pet.on("spawn", onSpawn)

while True:
    if skeleton.health > 0:
        hero.attack(skeleton)
    else:
        hero.moveXY(31, 38)
