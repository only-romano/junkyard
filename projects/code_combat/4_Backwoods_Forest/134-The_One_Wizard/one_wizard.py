while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        distance = hero.distanceTo(enemy)
        if distance <= 30:
            if hero.canCast("chain-lightning"):
                hero.cast("chain-lightning", enemy)
            else:
                if enemy.type == "ogre":
                    hero.moveXY(7, 42)
                else
                    hero.attack(enemy)
        else:
            if hero.canCast("lightning-bolt"):
                hero.cast("lightning-bolt", enemy)
            elif hero.canCast("regen"):
                hero.cast("regen", hero)
