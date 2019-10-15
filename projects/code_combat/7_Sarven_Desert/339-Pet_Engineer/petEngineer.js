// Move your pet to the left or right button as needed.

function onHear(event) {
    // Find the guards to listen to.
    var archer = pet.findNearestByType("archer");
    var soldier = pet.findNearestByType("soldier");
    // If event.speaker is the `archer`:
    if (event.speaker == archer) {
        // Move to the left button.
        pet.moveXY(32, 30);
    }
    // If event.speaker is the `soldier`:
    else if (event.speaker == soldier) {
        // Move to the right button.
        pet.moveXY(48, 30);
    }
}

pet.on("hear", onHear);

// You don't have to change the code below.
// Your hero should protect the bottom right passage.
while(true) {
    var enemy = hero.findNearestEnemy();

    // fix for running away hero
    if (enemy && hero.distanceTo(enemy) < 10)
        hero.attack(enemy);
    else
        hero.moveXY(60, 15);
}
