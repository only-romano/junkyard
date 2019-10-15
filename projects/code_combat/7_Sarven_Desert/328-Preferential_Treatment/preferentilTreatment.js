// First, loop through all enemies...

var enemies = hero.findEnemies();
var enemyIndex = 0;
// ... but only attack "thrower" type enemies.
while(enemyIndex < enemies.length) {
    var enemy = enemies[enemyIndex];
    if(enemy && enemy.type === "thrower") {
        hero.attack(enemy);
    }
    enemyIndex += 1;
}
// Then loop through all the enemies again...
enemies = hero.findEnemies();
enemyIndex = 0;
// ... and defeat everyone who's still standing.
while (enemyIndex < enemies.length) {
    var enemy = enemies[enemyIndex];
    if (hero.isReady("bash"))
        hero.bash(enemy);
    else hero.attack(enemy);
    enemyIndex++;
}
