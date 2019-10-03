// You can't help the peasants across the river.
// But, your pet can!
// Teach your wolf to be a guard dog.

function onSpawn(event) {
    while (true) {
        // Pets can find enemies, too.
        var enemy = pet.findNearestEnemy();
        // If there is an enemy:
        if (enemy) {
            // Then have the pet say something:
            pet.say("Ahoy!");
        }
    }
}

pet.on("spawn", onSpawn);
