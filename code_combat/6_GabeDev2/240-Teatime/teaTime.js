// Use timers to spawn enemies and items.

// This spawns two aggressive munchkins.
function spawnMunchkins() {
    var munchkin1 = game.spawnXY("munchkin", 2, 12);
    var munchkin2 = game.spawnXY("munchkin", 2, 56);
    munchkin1.behavior = "AttacksNearest";
    munchkin2.behavior = "AttacksNearest";
}

// This spawns two aggressive throwers.
function spawnThrowers() {
    var thrower1 = game.spawnXY("thrower", 2, 16);
    var thrower2 = game.spawnXY("thrower", 2, 52);
    thrower1.behavior = "AttacksNearest";
    thrower2.behavior = "AttacksNearest";
}

// This spawns a health potion near the village.
function spawnPotion() {
    game.spawnXY("potion-large", 46, 34);
}

// Survive 30 seconds.
game.addSurviveGoal(20);

// The inital values of timers define the first appearance.
game.munchkinSpawnTime = 0;
game.throwerSpawnTime = 0;
game.potionSpawnTime = 6;
// This is used for UI.
game.nextPotionIn = 0;

ui.track(game, "time");
// Lets show how long until the next potion.
ui.track(game, "nextPotionIn");

var player = game.spawnPlayerXY("duelist", 40, 34);
player.maxSpeed = 15;

// This checks and updates timers.
function updateTimers() {
    // If game time is greater than the munchkinSpawnTime
    if (game.time > game.munchkinSpawnTime) {
        // Update the timer and spawn the munchkins.
        game.munchkinSpawnTime = game.munchkinSpawnTime + 6;
        spawnMunchkins();
    }
    // If game time is greater than potionSpawnTime
    if (game.time > game.potionSpawnTime) {
        player.say("The potion is here!");
        // Increase game.potionSpawnTime by 6:
        game.potionSpawnTime = game.potionSpawnTime + 6;
        // Call the spawnPotion function:
        spawnPotion();
    }
    // If game time is greater than throwerSpawnTime:
    if (game.time > game.throwerSpawnTime) {
        // Increase game.throwerSpawnTime by 9:
        game.throwerSpawnTime += 9;
        // Call the spawnThrowers function:
        spawnThrowers();
    }
    // Update the UI timer until the next potion
    game.nextPotionIn = game.potionSpawnTime - game.time;
}
    
while (true) {
    updateTimers();
}
