// Alejandro likes a challenge!
// Add more "forest" objects to the level to create a long maze.

// Set up the game's goal.
game.addCollectGoal();

// Spawn a hero and chest to collect.
game.spawnPlayerXY("duelist", 9, 59);
game.spawnXY("chest", 8, 14);

game.spawnXY("forest", 26, 51);
// Add 2 more "forest" objects. Make sure not to block the gems completely!
game.spawnXY("forest", 34, 22);
game.spawnXY("forest", 50, 22);
