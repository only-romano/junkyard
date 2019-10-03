// Your pet should run back and forth on the X marks.
// The hero should cheer the whole time!

// Write the event function onSpawn for the pet.
// This function should make the wolf run back and forth:
// First, run to the right mark, then the left one:
function onSpawn() {
    while(true) {
        pet.moveXY(48, 8);
        pet.moveXY(12, 8);
    }
}

pet.on("spawn", onSpawn);
// Cheer up your pet. Don't remove this:
while (true) {
    hero.say("Run!!!");
    hero.say("Faster!");
}
