def onSpawn(event):
    pet.moveXY(22, 10)
    pet.moveXY(71, 10)
    pet.moveXY(71, 57)
    pet.moveXY(20, 57)
    pet.moveXY(20, 20)

items = hero.findItems()
pet.on("spawn", onSpawn);

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        if hero.isReady("cleave"):
            hero.cleave(enemy)
        elif hero.isReady("bash"):
            hero.bash(enemy)
        else:
            hero.attack(enemy)
        hero.moveXY(23, 36)
    if hero.gold >= 290:
        hero.moveXY(50, 34)
