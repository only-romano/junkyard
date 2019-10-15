// You must to find the treasure.

// This function should return the index of a letter:
function letterIndex(word, letter) {
    // Step through each letter as an index of the word.
    for (var i = 0; i < word.length; i++) {
        // Store a character from the word with the current index.
        var character = word[i];
        // If it is the required letter:
        if (character === letter)
            // Then return the current index (number).
            return i;
    }
    // If nothing, return a default value
    return -1;
}

var ogreLetter = "z";
var shaman = hero.findByType("thoktar")[0];

// Find the index and use it for finding the treasure.
var chestIndex = letterIndex(shaman.id, ogreLetter);
hero.moveXY(16 + chestIndex * 8, 36);
