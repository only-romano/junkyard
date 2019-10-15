// The treasure somewhere between trees.
// The coordinates are 'x: ?0, y: ?0'. 
// Move at all potential points and show to peasants where to dig.

var leftBorder = 20;
var rightBorder = 61;
var bottomBorder = 20;
var topBorder = 51;
var step = 10;

// Iterate X coordinates from the left to right border with step 10.
for (var x = leftBorder; x < rightBorder; x += step) {
    // Use a nested loop to iterate through Y coordinates for each X.
    // Iterate y coordinates from the bottom to top border with step 10.
    for (var y = bottomBorder; y < topBorder; y += 10) {
        // Move to the point with coordinates X, Y and say anything.
        hero.moveXY(x, y);
        hero.say("Anything");
    }
}

// Allow peasants to check the last point.
hero.moveXY(20, 10);
