// Find the hidden number in the agent's message to escape.
// Count the number of trailing and leading whitespaces.

// This function returns the coordinates of the n-th passage.
function passagePosByNum(n) {
    return {x: 60, y: n * 12 + 8};
}

function onHear(event) {
    // The original message.
    var message = event.message;
    // Trim the message:
    var trimmed = message.trim();
    // The hidden number is the difference of lengths:
    var hidden = message.length - trimmed.length;
    // Use passagePosByNum to find the passage to enter:
    var pos = passagePosByNum(hidden);
    // Move the pet to the entrance of the passage:
    pet.moveXY(pos.x, pos.y);
    // Move the pet to the left edge of the map:
    pet.moveXY(2, pos.y);
}

pet.on("hear", onHear);

// The hero should follow the pet.
while(true) {
    hero.move(pet.pos);
}
