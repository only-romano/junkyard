// There are four pairs of twins, they should pray by pairs.
// You need to find twins and call them.

// Twins have the same names, only the last letter is different.
// This function checks if the pair of units are twins.
function areTwins(unit1, unit2) {
    var name1 = unit1.id;
    var name2 = unit2.id;
    if (name1.length !== name2.length) {
        return false;
    }
    for (var i = 0; i < name1.length - 1; i++) {
        if (name1[i] !== name2[i]) {
            return false;
        }
    }
    return true;
}

// Iterate over all pairs of paladins and
//  say() their name by pairs if they are twins.
var paladins = hero.findByType("paladin");
// For example: hero.say("NameTwin1 NameTwin2")
for (var i = 0; i < paladins.length; i++) {
    for (var j = 0; j < paladins.length; j++) {
        if (i == j)
            continue;
        if (areTwins(paladins[i], paladins[j]))
            hero.say(paladins[i].id + " " + paladins[j].id);
    }
}
// When twins are in their spots, lure the ogre.
// Don't be afraid of beams - they are dangerous only for ogres.
hero.moveXY(65, 36);
hero.moveXY(13, 36);
