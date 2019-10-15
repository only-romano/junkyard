while True:
    enemy = hero.findNearestEnemy()
    distance = 0
    if enemy:
        distance = hero.distanceTo(enemy)
    if distance < 10 and hero.isReady("cleave"):
        hero.cleave(enemy)
    else if distance < 5:
        hero.attack(enemy)
    else
        hero.attack("Chest")
