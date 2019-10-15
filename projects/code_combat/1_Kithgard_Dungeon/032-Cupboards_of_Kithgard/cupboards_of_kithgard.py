# You need the Elemental codex 1+ to cast "Haste"
# You need the Emperor's gloves to cast "Chain Lightning"
# You need an unique hero to use "Mana Blast"

hero.attack("Cupboard")
hero.cast("haste", hero)
hero.moveUp()
hero.moveRight(4)
hero.manaBlast()
var enemy = hero.findNearestEnemy();
hero.cast("chain-lightning", enemy);
