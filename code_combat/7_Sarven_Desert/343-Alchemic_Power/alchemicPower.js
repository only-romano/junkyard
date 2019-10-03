// Wait for alchemist's commands to fetch potions.

// The event handler for the pet's event "hear".
function onHear(event) {
    // Find the nearest potion.
    var potion = pet.findNearestByType("potion");
    var message = event.message;
    // If the event's message is "Fetch"
    if (message == "Fetch") {
        // Have the pet fetch the potion.
        pet.fetch(potion);
    }
    // Else (for any other messages):
    else {
        // Use pet.moveXY to return the pet to the red mark.
        pet.moveXY(54, 34);
    }
}

pet.on("hear", onHear);

// You don't have to change the code below.
while(true) {
    var enemies = hero.findEnemies();

    // Fix for weak hero
    var max = 0;
    var strongest = null;
    for (var i = 0; i < enemies.length; i++) {
        var enemy = enemies[i];
        if (enemy.health > max) {
            max = enemy.health;
            strongest = enemy;
        }
    }
    if (strongest) {
        while (strongest.health > 0)
            hero.attack(strongest);
    }
    else {
        hero.moveXY(40, 34);
    }
}
