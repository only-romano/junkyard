def onSpawn (event):
    while True:
        item = hero.findNearestItem()
        if item:
            pet.fetch(item)

pet.on("spawn", onSpawn)

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        if hero.canCast("chain-lightning"):
            hero.cast("chain-lightning", enemy)
        else:
            hero.attack(enemy)
