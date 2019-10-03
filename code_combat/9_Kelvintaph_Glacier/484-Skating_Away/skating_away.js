// Move to the red X mark while avoiding the yaks.
// use Vector.normalize(vector1) to create a vector in the same direction as vector1, but with a distance of 1
// use Vector.multiply(vector1, X) to create a vector in the same direction as vector1, but with its distance multiplied by X

// The point you want to get to.
var goalPoint = new Vector(78, 34);

while(true) {
    // This creates a vector that will move you 10 meters toward the goalPoint
    // First, create a vector from your hero to the goal point.
    var goal = Vector.subtract(goalPoint, hero.pos);
    // Then, normalize it into a 1m distance vector
    goal = Vector.normalize(goal);
    // Finally, multiply the 1m vector by 10, to get a 10m long vector.
    goal = Vector.multiply(goal, 10);
    
    // To avoid the yaks, if you get within 10 meters of a yak, you should vector away from it.
    var yak = hero.findNearest(hero.findEnemies());
    var distance = hero.distanceTo(yak);
    if(distance < 10) {
        // First, make a Vector from the yak to you
        var way = Vector.subtract(hero.pos, yak.pos);
        // Now use Vector.normalize and Vector.multiply to make it 10m long
        way = Vector.normalize(way);
        way = Vector.multiply(way, 10);
        // Once you have the 10m vector away from the yak, use Vector.add to add it to your goal vector!
        goal = Vector.add(goal, way);
    }
    // Finally, determine where to move by adding your goal vector to your current position.
    var moveToPos = Vector.add(hero.pos, goal);
    hero.move(moveToPos);
}
