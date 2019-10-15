// Each game must have a player and a goal.

// Use game.spawnPlayerXY("captain", x, y)
// to add a player to your game:
game.spawnPlayerXY('captain', 22, 14);
// Use game.addMoveGoalXY(x, y)
// to add a movement goal to your game:
// it should be 10m away from the player.
game.addMoveGoalXY(22, 24);

// If you want to, use spawnXY("fence", x, y)
// to make a maze with fences...
game.spawnXY("fence", 22, 19);  // hardcore mode

// Then, click "Test Level" to try your first playable game!
