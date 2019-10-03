# You need the Emperor's gloves to cast "Chain-lightning"
# You need Pender hero to perform Reset Cooldown

hero.cast("chain-lightning", hero.findNearestEnemy())
hero.resetCooldown("chain-lightning")
hero.cast("chain-lightning", hero.findNearestEnemy())
