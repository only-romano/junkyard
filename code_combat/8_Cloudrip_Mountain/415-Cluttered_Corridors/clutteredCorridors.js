// Help the pet find the exit.

function onHear(event) {
    var word = event.message;
    // Convert the word to lower case.
    word = word.toLowerCase();
    if (word == "north") {
        pet.moveXY(pet.pos.x, pet.pos.y + 16);
    }
    else if (word == "east") {
        pet.moveXY(pet.pos.x + 12, pet.pos.y);
    }
    else if (word == "south") {
        pet.moveXY(pet.pos.x, pet.pos.y - 16);
    }
    else if (word == "west") {
        pet.moveXY(pet.pos.x - 12, pet.pos.y);
    }
    
}

// Assign the event handler for the pet's "hear" event.
pet.on("hear", onHear);
