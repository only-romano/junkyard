# You need the Elemental codex 1+ to cast "Haste"
# You need the Emperor's gloves to cast "Chain Lightning"

hero.cast("haste", hero);
hero.attack(hero.findNearestEnemy());
hero.moveRight(3);
hero.cast("chain-lightning", hero.findNearestEnemy());
