// Players like seeing score, so use ui.track()!
// It will create a user-interface element for them to see.
var player = game.spawnPlayerXY("samurai", 20, 20);

game.addSurviveGoal(20);

var spawner = game.spawnXY("generator", 50, 50);
spawner.maxHealth = 9001;
spawner.spawnType = "munchkin";
// Add more spawners for more enemies on the field:
var spawner2 = game.spawnXY("generator", 50, 50);
spawner2.maxHealth = 9001;
spawner2.spawnType = "munchkin";
var spawner3 = game.spawnXY("generator", 50, 50);
spawner3.maxHealth = 9001;
spawner3.spawnType = "munchkin";

// ui.track() displays an object's property for players to see!
ui.track(game, "time");
// Use ui.track to track game's "defeated" property:
ui.track(game, "defeated");
player.attackDamage = 10;
// Increase the hero's maxSpeed:
player.maxSpeed = 10;
// Press play and defeat 6 munchkins or skeletons!
