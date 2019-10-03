// Anya is searching for gems!
// Add gems to the level for the player to find.
// You must be able to beat your level to continue.

game.spawnPlayerXY("captain", 9, 18);
// Add a goal to collect the gems using game.addCollectGoal()
game.addCollectGoal(4);
game.spawnXY("gem", 28, 28);
// Spawn 3 gems across the level for the player to collect:
game.spawnXY("gem", 70, 10);
game.spawnXY("gem", 45, 43);
game.spawnXY("gem", 9, 35);
