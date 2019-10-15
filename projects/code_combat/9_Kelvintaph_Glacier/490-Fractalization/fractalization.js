// Check the guide for the description of the problem
// Here are some functions to help draw the curves.

function degreesToRadians(degrees) {
    // All vector operations require working in radians rather than degrees.
    return Math.PI / 180 * degrees;
}    

function koch(start, end) {
    // This function will draw a Koch Curve between two Vector positions
    // Start by creating a vector from start to end using Vector.subtract.
    // var full = ...
    var full = Vector.subtract(end, start);
    var magnitude = full.magnitude();
    
    // Use the magnitude of the vector to check for the stop condition.
    if (magnitude < 3) {
        // Move into position and draw the line, don't forget to toggle flowers properly.
        hero.toggleFlowers(false);
        hero.moveXY(start.x, start.y);
        hero.toggleFlowers(true);
        hero.moveXY(end.x, end.y);
        return;
    }
    
    // Need to draw 4 shorter Koch curves with sides 1/3 the length.
    // We will calculate the 3 intermediate points, A, B, & C.
    // We just need the point that is one-third of the full Vector from the start Vector.
    var third = Vector.multiply(full, 1 / 3);
    var A = Vector.add(start, third);
    // This one needs to be rotated 60 degrees from A but the same length.  Use rotate and add to get B.
    var B = Vector.add(A, Vector.rotate(third, degreesToRadians(60)));
    // This point works out to adding another third to A.
    var C = Vector.add(A, third);
    // Now we can draw the 4 curves connecting start, A, B, C, and end.
    koch(start, A);
    koch(A, B);
    koch(B, C);
    koch(C, end);

}

var whiteXs = [new Vector(6, 6), new Vector(74, 6), new Vector(74, 61), new Vector(6, 61)];

for (var i = 0; i < whiteXs.length; i++)
    koch(whiteXs[i], whiteXs[i==3?0:i+1]);
