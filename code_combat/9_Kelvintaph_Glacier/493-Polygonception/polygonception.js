// You are on your own this time, I hope you have learned what you need from
// the previous fractal levels. Check the guide for help with what you need
// to do and with the math required for polygons.

// You need a function to convert degrees to radians. Multiply degrees by Math.PI / 180.
function degToRad(deg) {
    return deg * Math.PI / 180;
}

function drawLine(start, end) {
    hero.toggleFlowers(false);
    hero.moveXY(start.x, start.y);
    hero.toggleFlowers(true);
    hero.moveXY(end.x, end.y);
}

// Your polygon function should have 3 inputs: start, end, and sides.
function polygon(start, end, sides) {
    var full = Vector.subtract(end, start);
    var angle = 180 - (sides - 2) * 180 / sides;
    var length = full.magnitude();
    var recursive = length / 5 > 2;

    for (var i = 0; i < sides; i++) {
        if (i > 0) {
            start = end;
            end = Vector.add(end, Vector.rotate(full, degToRad(angle * i)));
        }

        drawLine(start, end);
        
        if (recursive) {
            var part = Vector.multiply(full, 1 / 5);
            var permEnd = Vector.add(end, Vector.rotate(part, degToRad(angle * (i+1))));
            polygon(end, permEnd, sides);
        }
    }
}

// Remember to make your polygon recursive, drawing extra polygons at every corner.


// To get the start and end position for each polygon, add startOffset and endOffset
// to the yak's position.
var startOffset = new Vector(-15, -15);
var endOffset = new Vector(15, -15);

// You need to loop through all the yaks, drawing a polygon for each. Yaks are enemies.
var enemies = hero.findEnemies();
for (var i = 0; i < enemies.length; i++) {
    var yak = enemies[i];
    var start = Vector.add(yak.pos, startOffset);
    var end = Vector.add(yak.pos, endOffset);
    var sides = yak.sides;
    polygon(start, end, sides);
}
