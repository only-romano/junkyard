# You need the Emperor's gloves to cast "Chain Lightning"
# You need Vine Stuff to summon Burl
# You need Unholy Tome V to summon Undead and cast Poison Cloud

var enemy = hero.findNearestEnemy();
hero.cast("summon-burl");
hero.cast("summon-undead");
hero.cast("chain-lightning", enemy);
hero.resetCooldown("chain-lightning");
hero.cast("chain-lightning", enemy);
hero.cast("poison-cloud", enemy);

