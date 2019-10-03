// You must defeat the ogres
// But they are using black magic!
// Only the highlander soldiers are immune.
// Find highlanders, their names always contain "mac"

var highlanderName = "mac";

// This function should search for a string inside of a word:
function wordInString(string, word) {
    var lenString = string.length;
    var lenWord = word.length;
    // Step through indexes (i) from 0 to (lenString - lenWord)
    for (var i = 0; i <= lenString - lenWord; i++) {
        // For each of them step through indexes (j) of the word length
        for (var j = 0; j < lenWord; j++) {
            // If [i + j]th letter of the string is not equal [j]th letter of word, then break loop
            if (string[i + j] !== word[j])
                break;
            // if this is the last letter of the word (j == lenWord - 1), then return true.
            if (j === lenWord - 1)
                return true;
        }
    // If loops are ended then the word is not inside the string. Return False.
    }
    return false; // ∆ Remove this when the function is written.
}

// Look at your soldiers and choose highlanders only
var soldiers = hero.findFriends();
for (var i = 0; i < soldiers.length; i++) {
    var soldier = soldiers[i];
    if (wordInString(soldier.id, highlanderName)) {
        hero.say(soldier.id + " be ready.");
    }
}

// 
hero.say("ATTACK!!!");
