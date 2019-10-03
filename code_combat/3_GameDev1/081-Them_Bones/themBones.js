// Generators spawn enemies over time.
// Skeletons are afraid of lightstones.

var player = game.spawnPlayerXY("champion", 15, 35);
player.attackDamage = 60;
player.maxSpeed = 8;

game.addSurviveGoal();
game.addDefeatGoal();
game.spawnXY("x-mark-stone", 60, 35);
// Spawn a "generator"
game.spawnXY("generator", 40, 40);
// Spawn a "lightstone"
game.spawnXY("lightstone", 20, 30);
// Now beat your game!
