// Now you can create a custom goal for your game
// using the game.addManualGoal(description) method!

// Spawn a few scouts, a boss, and a maze.
game.spawnMaze(5);
game.spawnXY("scout", 60, 58);
game.spawnXY("scout", 28, 29);
game.spawnXY("scout", 61, 24);
var ogref = game.spawnXY("ogre-f", 60, 12);

// Spawn and configure the hero.
var hero = game.spawnPlayerXY("captain", 12, 56);
hero.maxHealth = 550;
hero.maxSpeed = 10;
hero.attackDamage = 25;

// Spawn a munchkin generator.
var generator = game.spawnXY("generator", 41, 13);
generator.spawnDelay = 5;
generator.spawnType = "munchkin";

// Survive goal.
game.addSurviveGoal();
game.spawnXY("potion-medium", 28, 12);

// addManualGoal adds an incomplete goal with a description
// The description will be shown to players.
// NOTE that we save it in a variable called scoutGoal
var scoutGoal = game.addManualGoal("Defeat all scouts");

// Use addManualGoal to add a goal to defeat the boss
// Save it in a variable called bossGoal
var bossGoal = game.addManualGoal("Defeat big Boss");

// Enemy Behavior
function onSpawn(event) {
    var unit = event.target;
    while(true) {
        var enemy = unit.findNearestEnemy();
        if(enemy) {
            unit.attack(enemy);
        }
    }
}
game.setActionFor("scout", "spawn", onSpawn);
game.setActionFor("ogre", "spawn", onSpawn);

// Count how many scouts are defeated.
var scoutsDefeated = 0;

// Update our manual goals whenever an enemy is defeated.
// This is an example of an algorithm using if-statements.
function onDefeat(event) {
    var unit = event.target;
    if (unit.type == "scout") {
        scoutsDefeated += 1;
        hero.say("Scout down!");
    }
    if (scoutsDefeated >= 3) {
        // Use setGoalState to mark scoutGoal complete.
        game.setGoalState(scoutGoal, true);
        hero.say("All Scouts down!");
    }
    if (unit.type == "ogre") {
        // Use game.setGoalState to mark bossGoal complete.
        // Don't forget about the second parameter.
        game.setGoalState(bossGoal, true);
        hero.say("Defeated the big boss!");
    }
}

// Assign the onDefeat handler to the ogres" "defeat"
// NOTE that munchkins don't count toward success!
game.setActionFor("scout", "defeat", onDefeat);
game.setActionFor("ogre", "defeat", onDefeat);
