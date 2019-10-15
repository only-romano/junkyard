// This array contains each of the pen's positions.
var penPositions = [
    {"x":20,"y":24},
    {"x":28,"y":24},
    {"x":36,"y":24},
    {"x":44,"y":24},
    {"x":52,"y":24}
];

// This array is used to track which reindeer is in it.
var penOccupants = [ "empty", "empty", "empty", "empty", "empty" ];

// And this array contains our reindeer.
var friends = hero.findFriends();

// Figure out which reindeer are already in their pens.
for (var deerIndex = 0; deerIndex < friends.length; deerIndex++) {
    var reindeer = friends[deerIndex];

    // Check each pen if it matches a reindeer's pos.
    for (var penIndex = 0; penIndex < penPositions.length; penIndex++) {
        var penPos = penPositions[penIndex];

        if (penPos.x == reindeer.pos.x && penPos.y == reindeer.pos.y) {
            // Put the id in penOccupants at penIndex.
            penOccupants[penIndex] = reindeer.id;
            // break out of the inner loop here.
            break;
        }
    }
}

// Tell Merek what's in each pen.
for (var occIndex = 0; occIndex < penOccupants.length; occIndex++) {
    // Tell Merek the pen index and the occupant.
    // Say something like "Pen 3 is Dasher"
    hero.say("Pen " + occIndex + " is "  + penOccupants[occIndex]);
}
