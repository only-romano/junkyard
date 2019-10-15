// You need to guess the number from 1 to 999 (0 < n < 1000).
// You have 10 attempts!
// For each attempt Riddler will say if the number is less or greater.
// If the guessed number is less than your try, then a munchkin ogre appears.
// Else a scout ogre appears.

var lowestPossible = 1;
var highestPossible = 999;
var num = 0;

while (true) {
    // You need to defeat the enemy before the next attempt.
    var enemy = hero.findNearest(hero.findEnemies());
    if (enemy) {
        // "scout" is 'greater', "munchkin" is less.
        // Prepare for the next attempt and wipe out the ogre.
        if (enemy.type == "scout")
            lowestPossible = num;
        else if (enemy.type == "munchkin")
            highestPossible = num;
        hero.attack(enemy);
    }
    else {
        // Make your next attempt and say it.
        num = lowestPossible + Math.ceil((highestPossible - lowestPossible) / 2);
        hero.say(num);
    }
}
