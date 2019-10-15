// Mirror your partner's movement around the center X mark.
// Vectors can be thought of as an x, y position
// Vectors can also represent the distance and direction between two positions

// use Vector.subtract(vector1, vector2) to find the direction and distance from vector2 to vector1
// use Vector.add(vector1, vector2) to find the position you get when you start from vector1 and follow vector2

// Create a new Vector at the center X point
var center = new Vector(40, 34);

// A unit's position is actually a Vector!
var partner = hero.findByType("peasant")[0];

while(true) {
    // First, you want to find the Vector (distance and direction) of the partner's position to the center X.
    var vector = Vector.subtract(center, partner.pos);

    // Second, find the position your hero should moveTo starting from center, and following vector.
    var moveToPos = Vector.add(center, vector);

    // Third, move to the moveToPos position.
    hero.move(moveToPos);
}
