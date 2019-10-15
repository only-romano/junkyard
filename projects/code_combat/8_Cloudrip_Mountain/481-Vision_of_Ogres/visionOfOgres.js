// Destroy a real ogre and illusions will disappear.

function findRealEnemy(enemies) {
    for (var index = 0; index < enemies.length; index++) {
        var enemy = enemies[index];
        // Convert the enemy's name (id) to lower case
        // and save it in a variable.
        var name = enemy.id.toLowerCase();
        // Split the name by whitespaces and save the words.
        var words = name.split(" ");
        // Store the second word in a variable.
        var second = words[1];
        // If the first letter of the second word equals to
        // the last letter of that word.
        if (second[0] == second[second.length - 1])
            // Then it's the real one. Return the enemy.
            return enemy;
    }
}

// Only attack real ogres.
while(true) {
    var ogres = hero.findEnemies();
    var realOgre = findRealEnemy(ogres);
    if (realOgre) {
        while(realOgre.health > 0) {
            hero.attack(realOgre);
        }
    }
}
