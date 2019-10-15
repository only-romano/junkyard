// Defeat the ogres and cure the hero.

// The pet is your only hope.
function onSpawn(e) {
    while(true) {
        var enemy = pet.findNearestByType("munchkin");
        if (enemy && pet.isReady("chase")) {
            pet.chase(enemy);
        }
        // Find and fetch a "potion":
        var potion = pet.findNearestByType("potion");
        if (potion) {
            pet.fetch(potion);
        }
    }
}

// Assign "onSpawn" handler on the "spawn" event:
pet.on("spawn", onSpawn);
