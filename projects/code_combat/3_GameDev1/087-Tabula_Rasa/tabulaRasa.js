// Create your own game!
game.spawnMaze("forest", 4);
// Spawn a player with spawnPlayerXY(type, x, y)
var player = game.spawnPlayerXY('captain', 60, 10);
player.maxSpeed = 7;
// Add at least one goal!
game.addCollectGoal(3);
game.addDefeatGoal(3);

// Spawn objects into the game with spawnXY(type, x, y)
game.spawnXY("munchkin", 12, 35);
game.spawnXY("munchkin", 52, 59);
game.spawnXY("munchkin", 36, 11);
game.spawnXY("skeleton", 60, 45);
game.spawnXY("skeleton", 28, 25);
game.spawnXY("skeleton", 12, 58);
game.spawnXY("skeleton", 28, 45);

game.spawnXY("gem", 60, 59);
game.spawnXY("gem", 12, 12);
game.spawnXY("gem", 28, 58);

game.spawnXY("lightstone", 12, 27);
