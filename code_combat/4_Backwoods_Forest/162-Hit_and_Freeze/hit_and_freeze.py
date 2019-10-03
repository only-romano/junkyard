def inAttackRange(enemy):
    return hero.distanceTo(enemy) <= 3

while True:
    enemy = hero.findNearestEnemy()
    if hero.canCast("chain-lightning")
        hero.cast("chain-lightning", enemy)
    elif inAttackRange(enemy):
        if hero.isReady("cleave"):
            hero.cleave(enemy)
        else:
            hero.attack(enemy);
