// Use voice commands to command the artillery.

while(true) {
    var enemy = pet.findNearestEnemy();
    if(!enemy) {
        continue;
    }
    // Scouts are fast. We need stop them. 
    if(enemy.type == "scout") {
        var distance = pet.distanceTo(enemy);
        if(pet.isReady("cold-blast") &&  distance < 5) {
            pet.coldBlast();
        }
    }
    else {
        // If the enemy on the left of the pet:
        if (enemy.pos.x < pet.pos.x) {
            // Say  "left".
            pet.say("Left");
        }
        // If the enemy on the right of the pet:
        else {
            // Say  "right".
            pet.say("Right");
        }
    }
}
