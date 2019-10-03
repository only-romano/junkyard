def cleaveOrAttack(enemy):
    if hero.isReady("cleave"):
        hero.cleave(enemy)
    else:
        hero.attack(enemy)

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        distance = hero.distanceTo(enemy)
        if distance < 5:
            cleaveOrAttack(enemy)
