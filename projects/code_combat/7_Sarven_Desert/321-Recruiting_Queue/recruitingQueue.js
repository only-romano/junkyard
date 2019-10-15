// Call peasants one after another.

// Neutral units are detected as enemies.
var neutrals = hero.findEnemies();
while (true) {
    if (neutrals.length) {
        // Say the first unit in the neutrals array
        hero.say(neutrals[0]);
    } else {
        hero.say("Nobody here");
    }
    // Reassign the neutrals variable using findEnemies()
    neutrals = hero.findEnemies();
}
