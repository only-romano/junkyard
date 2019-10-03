// Get all swords and protect the village.

function onSpawn (event) {
    while(true) {
        var item = hero.findNearestItem();
        //  The pet should fetch the item if it exists:
        if (item) {
            pet.fetch(item);
        }
    }
}

// Assign onSpawn function for the pet's "spawn".
pet.on("spawn", onSpawn);

while(true) {
    // Guard the left passage: 
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        if (hero.canCast("chain-lightning")) {
            hero.cast("chain-lightning", enemy);
        } else if (hero.canCast("drain-life")) {
            hero.cast("drain-life", enemy);
        }
        hero.attack(enemy);
    }
}
