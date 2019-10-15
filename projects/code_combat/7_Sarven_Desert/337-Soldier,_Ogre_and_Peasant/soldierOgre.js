// Deliver that trinity to the left side of the river.

// The soldier hates the ogre.
var soldier = pet.findNearestByType("soldier");
// The ogre plans something bad against the peasant.
var ogre = pet.findNearestByType("munchkin");
// Just a peasant. 
var peasant = pet.findNearestByType("peasant");

// Use pet.carryUnit(unit, x, y) to deliver units.
pet.carryUnit(ogre, 32, 38);
pet.carryUnit(peasant, 32, 38);
pet.carryUnit(ogre, 53, 38);
pet.carryUnit(soldier, 32, 38);
pet.carryUnit(ogre, 32, 38);

