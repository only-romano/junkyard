// Spawn a maze. Change the number for a different maze!
game.spawnMaze("munchkin", 9);

// Spawn a hero with spawnPlayerXY(type, x, y)
game.spawnPlayerXY('captain', 60, 10);
game.spawnXY("gem", 30, 10);
game.spawnXY("gem", 45, 10);

// Add at least one goal!
game.addCollectGoal();
