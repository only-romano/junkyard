// The warlock used the "clone" spell and created evil antipodes of our archers.
// But even that evil spell has weakness.
// If your archer touches his antipode, then it will disappear.
// If an archer touches the wrong clone or attacks one of them, then the clones start to fight.
// We can find antipodes by their names - they are each other's reverse.

// This function check two units whether they are antipodes or not.
function areAntipodes(unit1, unit2) {
    var reversed1 = unit1.id.split("").reverse().join("");
    return reversed1 === unit2.id;
}

var friends = hero.findFriends();
var enemies = hero.findEnemies();

// Find antipodes for each of your archers.
// Iterate all friends.
for (var i = 0; i < friends.length; i++) {
    // For each of friends iterate all enemies.
    var friend = friends[i];
    for (var j = 0; j < enemies.length; j++) {
        // Check if the pair of the current friend and the enemy are antipodes.
        var enemy = enemies[j];
        if (areAntipodes(friend, enemy)) {
            // If they are antipodes, command the friend move to the enemy.
            hero.command(friend, "move", enemy.pos);
        }
    }
}
// When all clones disappears, attack the warlock.
hero.wait(5);
var warlock = hero.findByType("warlock")[0];
while (warlock.health > 0) {
    hero.attack(warlock);
}
