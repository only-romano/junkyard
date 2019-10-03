// Make your own game by changing the code below!
// Spawn a maze. Change the number for a different maze!
game.spawnMaze("fence", 88);

// Spawn a player with spawnPlayerXY()
var player = game.spawnPlayerXY("raider", 12, 12);
player.attackDamage = 10;
player.maxHealth = 200;


// Add at least one goal!
game.addCollectGoal();
game.addSurviveGoal();

// Spawn some things to collect!
game.spawnXY("gem", 28, 12);
game.spawnXY("gem", 60, 60);

// You need a key to collect a locked chest.
game.spawnXY("locked-chest", 44, 28);
game.spawnXY("silver-key", 52, 60);
game.spawnXY("potion-medium", 60, 12);

// Spawn some enemies!
var s1 = game.spawnXY("skeleton", 35, 60);
s1.behavior = "AttacksNearest";
var s2 = game.spawnXY("skeleton", 55, 60);
s2.behavior = "Defends";
game.spawnXY("lightstone", 45, 45);

var gen = game.spawnXY("generator", 12, 61);
gen.spawnType = "munchkin";
gen.spawnDelay = 5;

game.spawnXY("munchkin", 28, 19);
// Ogre Spear Throwers have a ranged attack!
game.spawnXY("thrower", 48, 28);
// This gargoyle shoots fire!
var spewer = game.spawnXY("fire-spewer", 28, 45);
spewer.direction = "horizontal";

// Track plays and ogres defeated in the database.
db.add("plays", 1);
ui.track(db, "plays");
ui.track(db, "defeated");

function onVictory(event) {
    db.add("defeated", game.defeated);
}

game.on("victory", onVictory);
