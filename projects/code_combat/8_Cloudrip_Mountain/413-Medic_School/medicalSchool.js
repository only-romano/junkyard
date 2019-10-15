// Collect 10 mushrooms.

// This function checks if the phrase starts with the word.
function startsWith(phrase, word) {
    // If the word is longer than the text, return false.
    if (word.length > phrase.length)
        return false;
    // Loop through the indexes of word and text.
    for (var i = 0; i < word.length; i++)
        // If characters with the same index are different:
        if (word[i] !== phrase[i])
            // Return false.
            return false;
    // We checked all letters and they are the same.
    // Return true.
    return true;
}


function onHear(event) {
    // Accept only options from experts.
    if (startsWith(event.speaker.id, "Exp")) {
        var potion = pet.findNearestByType("potion");
        if (potion) {
            pet.fetch(potion);
            pet.moveXY(28, 34);
        }
    }
}
pet.on("hear", onHear);
while(true) {
    var mushrooms = hero.findByType("mushroom");
    var nearest = hero.findNearest(mushrooms);
    if (nearest) {
        hero.moveXY(nearest.pos.x, nearest.pos.y);
    }
}
