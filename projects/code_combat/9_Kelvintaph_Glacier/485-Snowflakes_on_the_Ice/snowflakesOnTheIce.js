// For this level we need to a line fractal for the ground and a hexagonal snowflake made up
// of 6 line fractals. Check the guide for an image of the desired output.

function degreesToRadians(degrees) {
    // All vector operations require working in radians rather than degrees.
    return Math.PI / 180 * degrees;
}
    
// This function creates a line fractal.  Read through it so you understand the
// recursive concept.
function line(start, end) {
    // First we need to get the full vector and its magnitude to determine if we
    // are below our minimum threshold.
    var full = Vector.subtract(end, start);
    var distance = full.magnitude();
    if (distance < 4) {
        // If under our threshold distance, then we will simply draw a line along
        // the vector and be done (the return tells us to exit the function).
        hero.toggleFlowers(false);
        hero.moveXY(start.x, start.y);
        hero.toggleFlowers(true);
        hero.moveXY(end.x, end.y);
        return;
    }
        
    // Otherwise we will create our fractal by getting a vector of half magnitude.
    var half = Vector.divide(full, 2);
    
    // We will be creating 4 line fractals (start -> A, A -> B, B -> A, and A -> end)
    // and so we need to calculate the intermediate positions A and B.
    var A = Vector.add(half, start);
    
    // To get B, we need to rotate the vector half 90 degrees and multiply by 2/3
    // (so it is 1/3 of the original magnitude), then add this to A.
    var rotate = Vector.rotate(half, degreesToRadians(90));
    rotate = Vector.multiply(rotate, 2 / 3);
    var B = Vector.add(rotate, A);

    // Now just draw the 4 lines using the line functions.
    line(start, A);
    line(A, B);
    line(B, A);
    line(A, end);
}

function flake (start, end) {
    // To create a hexagonal flake we need to create 6 line fractals rotated by
    // 60 degrees each time.
    var side = Vector.subtract(end, start);
    var a = start;
    var b = end;
    for (var i = 0; i < 6; ++i) {
        line(a, b);
        // To get the next edge, we need to rotate the side 60 degrees.
        side = Vector.rotate(side, degreesToRadians(60));
        // Now need to reset a and b with the beginning and end points for the new side.
        a = b;
        b = Vector.add(side, a);
    }
}

var whiteXs = [new Vector(12, 10), new Vector(60, 10)];
var redXs = [new Vector(64, 52), new Vector(52, 52)];

// You need to actually call the functions with a start and end vector for each.
flake(redXs[0], redXs[1]);
// Be sure to use actual Vector objects–simple objects will not work.
line(whiteXs[0], whiteXs[1]);
// Refresh often to avoid a memory leak and crash (working on it)
