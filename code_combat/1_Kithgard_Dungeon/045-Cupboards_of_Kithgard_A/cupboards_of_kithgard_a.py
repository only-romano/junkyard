# You need the Elemental codex 1+ to cast "Haste"
# You need an unique hero to perform "Mana Blast"
# You need the Emperor's gloves to cast "Chain Lightning"

hero.cast("haste", hero)
hero.attack("Cupboard")
hero.moveDown()
hero.moveLeft(3.5)
hero.cast("chain-lightning", hero.findNearestEnemy())
hero.manaBlast()
