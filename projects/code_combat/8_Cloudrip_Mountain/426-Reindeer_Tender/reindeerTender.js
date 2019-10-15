// This is the array of pen positions
var penPositions = [ {"x":20,"y":24}, {"x":28,"y":24}, {"x":36,"y":24}, {"x":44,"y":24}, {"x":52,"y":24} ];

// Use this array to keep track of each pen's reindeer.
var penOccupants = [ null, null, null, null, null ];

// And this array contains our reindeer.
var friends = hero.findFriends();

// Figure out which reindeer are already in their pens.
for (var deerIndex = 0; deerIndex < friends.length; deerIndex++) {
    var reindeer = friends[deerIndex];
    
    // For each position check if it matches a reindeer.
    for (var penIndex = 0; penIndex < penPositions.length; penIndex++) {
        var penPos = penPositions[penIndex];
        
        if (penPos.x == reindeer.pos.x && penPos.y == reindeer.pos.y) {
            // Put the reindeer in occupants at penIndex
            penOccupants[penIndex] = reindeer;
            // Remove the reindeer from the friends array.
            friends[deerIndex] = null;
            // break out of the inner loop here:
            break;
        }
    }
}

// Assign the remaining reindeer to new positions.
for (deerIndex = 0; deerIndex < friends.length; deerIndex++) {
    // If the reindeer is null, use continue:
    var reindeer = friends[deerIndex];
    if (!reindeer)
        continue;
    
    // Look for the first pen with nothing.
    for (var occIndex = 0; occIndex < penOccupants.length; occIndex++) {
        // If there is nothing, the pen is open:
        if (penOccupants[occIndex] === null) {
            // Put the reindeer in the occupants array.
            penOccupants[occIndex] = reindeer;
            // Command the reindeer to move to the pen.
            hero.command(reindeer, "move", penPositions[occIndex]);
            // break out early so we don't reassign:
            break;
        }
    }
}
