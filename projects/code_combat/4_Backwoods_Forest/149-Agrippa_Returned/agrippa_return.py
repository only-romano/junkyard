def enemyInRange(enemy):
    return hero.distanceTo(enemy) < 5

def cleaveOrAttack(enemy):
    if hero.isReady("cleave"):
        hero.cleave(enemy)
    else:
        hero.attack(enemy)

while True:
    enemy = hero.findNearestEnemy()
    if enemy and enemyInRange(enemy):
        cleaveOrAttack(enemy)
