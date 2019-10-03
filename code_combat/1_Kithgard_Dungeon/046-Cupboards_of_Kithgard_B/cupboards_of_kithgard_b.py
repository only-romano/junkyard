# You need the Elemental codex 1+ to cast "Haste"
# You need an unique hero to perform "Mana Blast"
# You need the Emperor's gloves to cast "Chain Lightning"

hero.cast("haste", hero)
hero.attack("Cupboard")
hero.moveRight(0.7)
hero.moveDown()
hero.moveRight(2.6)
hero.cast("chain-lightning", hero.findNearestEnemy())
hero.manaBlast()
