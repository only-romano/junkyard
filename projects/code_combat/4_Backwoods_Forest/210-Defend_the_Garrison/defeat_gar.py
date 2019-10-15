# Unholy Tome 5 to "Poison Cloud", "Drain Life", "Raise Dead", "Fear", "Summon Undead"
# Emperor's ring to "Chain Lightning"
# Vine Staff to "Summon Burl"

while True:
    enemy = hero.findNearestEnemy()
    flag = hero.findFlag()

    if flag:
        hero.pickUpFlag(flag)

    if hero.canCast("summon-burl"):
        hero.cast("summon-burl")
    if hero.canCast("summon-undead"):
        hero.cast("summon-undead")

    if enemy:
        distance = hero.distanceTo(enemy)

        if distance <= 30:
            if hero.canCast("chain-lightning"):
                hero.cast("chain-lightning", enemy)
            elif distance > 15 and hero.canCast("poison-cloud"):
                hero.cast("poison-cloud", enemy)
            elif distance <= 25 and hero.canCast("fear"):
                hero.cast("fear", enemy)
            elif distance <= 15 and hero.canCast("drain-life"):
                hero.cast("drain-life", enemy)
            else:
                hero.attack(enemy)
        elif distance < 45:
            hero.attack(enemy)

    if hero.canCast("raise-dead"):
        hero.cast("raise-dead")
