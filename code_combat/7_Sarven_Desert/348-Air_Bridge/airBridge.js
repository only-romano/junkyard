// Help peasants to escape.

function onSpawn(e) {
    // We need to save three peasants.
    var remainingPeasants = 3;
    while (remainingPeasants > 0) {
        // Take a good position.
        pet.moveXY(40, 55);
        var peasant = pet.findNearestByType("peasant");
        if (peasant) {
            // Carry the peasant to the center passage.
            pet.carryUnit(peasant, 40, 34);
            remainingPeasants -= 1;
        }
    }
    var munchkin = pet.findNearestByType("munchkin");
    // Carry a munchkin to the fire traps:
    if (munchkin) {
        pet.carryUnit(munchkin, 41, 19);
    }
}

pet.on("spawn", onSpawn);

// Fight!
while (true) {
    var enemy = hero.findNearestEnemy();
    if (enemy && hero.distanceTo(enemy) < 10)
        hero.attack(enemy);
}
