# You need the Elemental codex 1+ to cast "Haste"
# You need the Emperor's gloves to cast "Chain Lightning"

hero.cast("haste", hero)
hero.moveUp()
hero.moveRight(2)
hero.moveUp()
hero.moveRight(4)
hero.moveUp(3)
hero.moveRight()

hero.cast("chain-lightning", hero.findNearestEnemy())
hero.resetCooldown("haste")
hero.cast("haste", hero)
hero.moveDown(3)
hero.moveLeft(5)
hero.moveDown(2)
