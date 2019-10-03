// Defeat the enemy hero in a duel!
hero.moveXY(43, 31);
var enemy = hero.findNearestEnemy();
pet.chase(enemy);

while(true) {
    // Find and attack the enemy inside a loop.
    // When you're done, submit to the multiplayer ladder!
    hero.attack(enemy);
    pet.chase(enemy);
    
}
