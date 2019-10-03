# You need the Elemental codex 1+ to cast "Haste"
# You need the Emperor's gloves to cast "Chain Lightning"

gemDude1 = hero.findNearestEnemy()
gemDude2 = hero.findNearestEnemy()

hero.cast("haste", hero)
hero.cast("chain-lightning", hero.findNearestEnemy())

hero.moveUp(0.9)
hero.moveRight(1.4)
