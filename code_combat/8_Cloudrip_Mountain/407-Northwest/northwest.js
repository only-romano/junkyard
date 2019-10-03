// Your pet should find and then bring the potion to the hero.

// This function checks if the word is in the text.
function wordInText(text, word) {
    // Iterate through each character in the text.
    for (var i = 0; i <= text.length - word.length; i++) {
        // For each of them loop through each character in word.
        for (var j = 0; j < word.length; j++) {
            // Store the shifted index i + j.
            var shiftedIndex = i + j;
            // If a character within the shifted index.
            // isn't equal to the character in word at the index "j"
            if (text[shiftedIndex] !== word[j])
                // Break the loop.
                break;
            // If j is equal to the index of the last letter in word
            if (j === word.length - 1)
                // Then the entire word is in the text.
                // Return true.
                return true;
        }
    }
    // The word was not found in text. Return false.
    return false;
}

// Follow the guides directions where to run.
function onHear(event) {
    // If "west" is in the phrase, the pet should run left.
    if (wordInText(event.message, "west")) {
        pet.moveXY(pet.pos.x - 28, pet.pos.y);
    }
    // If "north" is in the phrase, the pet should run up.
    else if (wordInText(event.message, "north")) {
        pet.moveXY(pet.pos.x, pet.pos.y + 24);
    } 
    // Else the pet should try to fetch the potion.
    else {
        var potion = pet.findNearestByType("potion");
        if (potion) {
            pet.fetch(potion);
        }
    }
}

pet.on("hear", onHear);
