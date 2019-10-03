# Not so cool solution but whatever
# You need the Vine Staff to summon Burl
# You need the Unholy Tome V to cast "Summon Undead", "Poison Cloud" & "Drain Life"
# You need Emperor's gloves to cast "Chain Lightning"

hero.moveRight(2)
hero.moveUp()
hero.moveRight(3)
hero.moveDown()
hero.moveRight()
hero.moveDown()
hero.moveRight(2)
hero.cast("summon-burl")
hero.cast("summon-undead")


while True:
    enemy = hero.findNearestEnemy()

    if enemy:
        distance = hero.distanceTo(enemy)
        if hero.canCast("chain-lightning") and distance < 30:
            hero.cast("chain-lightning", enemy)
        elif hero.isReady("reset-cooldown"):
            hero.resetCooldown("chain-lightning")
        elif hero.isReady("mana-blast"):
            hero.manaBlast()
        elif distance < 30 and hero.canCast("poison-cloud"):
            hero.cast("poison-cloud", enemy)
        elif distance < 15:
            hero.cast("drain-life", enemy)
        elif distance < 45:
            hero.attack(enemy)
