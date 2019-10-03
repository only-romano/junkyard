# You need the Elemental codex 1+ to cast "Haste"
# You need unique hero to perform resetCooldown action
# You need the Emperor's gloves to cast "Chain Lightning"

hero.cast("haste", hero)
hero.moveDown()
hero.moveRight()
hero.moveDown(0.5)
enemy = hero.findNearestEnemy()
hero.cast("chain-lightning", enemy)
hero.resetCooldown("chain-lightning")
hero.cast("chain-lightning", enemy)
