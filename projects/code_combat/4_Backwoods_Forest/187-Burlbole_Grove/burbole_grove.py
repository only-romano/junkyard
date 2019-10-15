def shouldAttack(target):
    return target and target.type != "burl"

while True:
    enemy = hero.findNearestEnemy()
    if shouldAttack(enemy):
        hero.attack(enemy)
