while True:
    polarPos = hero.time / 4
    xPos = 40 + Math.cos(polarPos) * 20
    yPos = 34 + Math.sin(polarPos) * 20
    hero.moveXY(xPos, yPos)

    enemy = hero.findNearestEnemy()
    if enemy:
        while enemy.health > 0:
            if hero.canCast("chain-lightning"):
                hero.cast("chain-lightning", enemy)  # fix for weak heroes required Emperor's gloves
            else:
                hero.attack(enemy)
