# You need the Elemental codex 1+ to cast "Haste"
# You need an unique hero to perform "Mana Blast"
# You need the Emperor's gloves to cast "Chain Lightning"

hero.cast("haste", hero)

hero.moveRight(0.8) or hero.moveUp(1) or hero.moveRight(0.9) or
hero.moveDown(1.2) or hero.moveUp(0.1) or hero.moveRight(1) or
hero.moveUp(1) or hero.moveRight(0.2)

hero.manaBlast()

hero.moveDown(0.1)

hero.resetCooldown("haste")

hero.cast("haste", hero)

hero.moveDown(1.2) or hero.moveUp(0.7) or hero.moveRight(1) or
hero.moveUp(0.9) or hero.moveRight(1) or hero.moveDown(1.8) or
hero.moveUp(0.7)

hero.cast("chain-lightning", hero.findNearestEnemy())

hero.moveRight(0.4)
