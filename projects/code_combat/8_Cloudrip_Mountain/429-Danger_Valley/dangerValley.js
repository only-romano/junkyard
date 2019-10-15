// Ogres have taken some peasants hostage!
// The scouts have given you intel for an ambush.
// this.grid holds an array of arrays.
// Inside the sub-arrays, 0 is a peasant, 1 is an ogre.
// Use this information to setup fire-traps.

// Remember the containing array is just an array!
// Iterate over all the elements of this array.
for(var i = 0; i < hero.grid.length; i++) {
    var row = hero.grid[i];
    // Now, row is just another array!
    // Iterate over all the tiles in this array:
    for (var j = 0; j < row.length; j++) {
        // Check if the tile at i, j is 1 to build:
        //hero.buildXY("fire-trap", 36 + 6 * j, 20 + 6 * i);
        if (row[j] == 1)
            hero.buildXY("fire-trap", 36 + 6 * j, 20 + 6 * i);
    }
}
// Finally, retreat back to cover.
hero.moveXY(29, 56);
