// Calculate the total health of all the ogres.

function sumHealth(enemies) {
    // Create a variable and set it to 0 to start the sum.
    var totalHealth = 0;
    // Initialize the loop index to 0
    var enemyIndex = 0;
    // While enemyIndex is less than the length of enemies array
    while (enemyIndex < enemies.length) {
        // Add the current enemy's health to totalHealth
        totalHealth += enemies[enemyIndex].health;
        // Increment enemyIndex by 1.
        enemyIndex += 1;
    }
    return totalHealth;
}

// Use the cannon to defeat the ogres.
var cannon = hero.findNearest(hero.findFriends());
// The cannon can see through the walls.
var enemies = cannon.findEnemies();
// Calculate the sum of the ogres' health.
var ogreSummaryHealth = sumHealth(enemies); 
hero.say("Use " + ogreSummaryHealth + " grams.");
