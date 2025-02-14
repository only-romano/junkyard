// We need to clear the forest of traps!
// The scout prepared a map of the forest.
// But be careful where you shoot! Don't start a fire.

// Get the map of the forest.
var forestMap = hero.findNearest(hero.findFriends()).forestMap;

// The map is a 2D array where 0 is a trap.
// The first sure shot.
hero.say("Row " + 0 + " Column " + 1 + " Fire!");

// But for the next points, check before shooting.
// There are an array of points to check.
var cells = [{row: 0, col: 4}, {row: 1, col: 0}, {row: 1, col: 2}, {row: 1, col: 4},
    {row: 2, col: 1}, {row: 2, col: 3}, {row: 2, col: 5}, {row: 3, col: 0},
    {row: 3, col: 2}, {row: 3, col: 4}, {row: 4, col: 1}, {row: 4, col: 2},
    {row: 4, col: 3}, {row: 5, col: 0}, {row: 5, col: 3}, {row: 5, col: 5},
    {row: 6, col: 1}, {row: 6, col: 3}, {row: 6, col: 4}, {row: 7, col: 0}];

for (var i = 0; i < cells.length; i++) {
    var row = cells[i].row;
    var col = cells[i].col;
    // If row is less than forestMap length:
    if (row < forestMap.length)
        // If col is less than forestMap[row] length:
        if (col < forestMap[row].length)
            // Now, we know the cell exists.
            // If it is 0, say where to shoot:
            if (forestMap[row][col] === 0)
                hero.say("Row " + row + " Column " + col + " Fire!");
}
