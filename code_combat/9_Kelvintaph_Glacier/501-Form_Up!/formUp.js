// Those soldiers before the gate are new recruits, and aren't trained.
// We should order them by their height.
// Their 'health' property is proportional to their height.
// Form up them from the smallest to the biggest (from left to right).
// Command those 8 recruits to move on the marks in the right order.

// This function returns the coordinates of the i-th mark.
function markPos(i) {
    return {x: 12 + i * 8, y: 12};
}

// This function returns a list of the soldiers who should be sorted.
function findUnplacedSoldiers() {
    var friends = hero.findFriends();
    var result = [];
    for (var i = 0; i < friends.length; i++) {
        var friend = friends[i];
        // Recruits' actions are readable.
        if (friend.pos.y < 30 && friend.pos.y > 18 && friend.action === "idle") {
            result.push(friend);
        }
    }
    return result;
}

// This function should return the unit with the least health.
function minHealthUnit(units) {
    // Write this function to use it for the sorting.
    var smallest = null;
    var lessHealth = Infinity;
    for (var i = 0; i < units.length; i++) {
        var unit = units[i];
        if (unit.health < lessHealth) {
            smallest = unit;
            lessHealth = unit.health;
        }
    }
    return smallest;
}

// Soldiers who should be sorted.
var recruits = findUnplacedSoldiers();
var markIndex = 0;

// While there are soldiers who aren't in the position.
while (recruits.length) {
    hero.say(recruits.length + " recruits aren't in the positions.");
    // Find the recruit with the minimum health.
    var smallest = minHealthUnit(recruits);
    // Command him to move to the mark (use 'markPos' function and 'markIndex').
    if (smallest)
        hero.command(smallest, "move", markPos(markIndex));
    // Increase markIndex by 1.
    markIndex += 1;
    // Update the list of soldiers who should be sorted - 'recruits'.
    recruits = findUnplacedSoldiers();
}
