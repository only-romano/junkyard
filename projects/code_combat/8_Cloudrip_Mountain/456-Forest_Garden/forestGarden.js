// Grow the perfect rectangular flower fence.

// Use the given dimensions for the flower rectangle.
var gardener = hero.findNearest(hero.findFriends());
var gardenWidth = gardener.gardenWidth;
var gardenHeight = gardener.gardenHeight;
// Start the flower fence at the initial position.
hero.toggleFlowers(true);
var x = hero.pos.x;
var y = hero.pos.y;
// Use variables gardenWidth and gardenHeight to get corners' coordinates.
// Move to each corner, one by one, and return to the start:
hero.moveXY(x, y - gardenHeight);
hero.moveXY(x + gardenWidth, y - gardenHeight);
hero.moveXY(x + gardenWidth, y);
hero.moveXY(x, y);
