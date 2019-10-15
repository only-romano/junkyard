# You need the Emperor's gloves to cast "Chain lightning"
# You need an Elemental Codex 1+ to cast "Haste"

hero.cast("haste", hero)
items = hero.findItems()
for item in items:
    hero.moveXY(item.pos.x, item.pos.y)

hero.cast("chain-lightning", hero.findNearestEnemy())
