while True:
    enemy = pet.findNearestEnemy()
    if not enemy:
        continue
    
    if enemy.type == "scout":
        if pet.isReady("cold-blast") and pet.distanceTo(enemy) < 5:
            pet.coldBlast()
    else:
        if enemy.pos.x < pet.pos.x:
            pet.say("Left")
        else:
            pet.say("Right")
