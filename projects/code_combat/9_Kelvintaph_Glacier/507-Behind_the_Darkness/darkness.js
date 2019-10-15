// Survive 70 seconds.

// The function allows you to wait for an ability.
function waitForAndAttack(abilityName) {
    while (true) {
        if (hero.isReady(abilityName)) {
            break;
        }
        var enemy = hero.findNearestEnemy();
        if (enemy && enemy.type !== "yeti" && hero.distanceTo(enemy) < 15) {
            hero.attack(enemy);
        }
    }
}
var SE = {x: 52, y: 20};
var NE = {x: 52, y: 48};
var NW = {x: 28, y: 48};
var SW = {x: 28, y: 20};
// Summon the Wall of Darkness to protect yourself.
// First, the east, north, and west sides.
// The order is important!
hero.wallOfDarkness([SW, NW, NE, SE]);
// Wait for "wall-of-darkness" and attack incoming ogres.
waitForAndAttack("wall-of-darkness");
// Second, summon the wall to the east and south sides:
hero.wallOfDarkness([NE, SE, SW]);

// Wait for "wall-of-darkness" and attack incoming ogres.
waitForAndAttack("wall-of-darkness");

// Third, the north and west sides:
hero.wallOfDarkness([NE, NW, SW]);

// Wait for "wall-of-darkness" and attack incoming ogres.
waitForAndAttack("wall-of-darkness");
