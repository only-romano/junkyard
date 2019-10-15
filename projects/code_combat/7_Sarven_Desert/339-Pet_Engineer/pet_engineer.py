def onHear(event):
    archer = pet.findNearestByType("archer")
    soldier = pet.findNearestByType("soldier")
    if event.speaker == archer:
        pet.moveXY(32, 30)
    elif event.speaker == "soldier":
        pet.moveXY(48, 30)

pet.on("hear", onHear)

while True:
    enemy = hero.findNearestEnemy()

    # fix for running away hero
    if enemy && hero.distanceTo(enemy) < 15:
        hero.attack(enemy)
    else:
        hero.moveXY(60, 15)
