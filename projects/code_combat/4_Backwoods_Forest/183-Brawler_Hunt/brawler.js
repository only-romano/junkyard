// Don't worry about small and medium-sized ogres.
// Your targets are type "brawler".
// When a "brawler" is closer than 50m, fire artillery.

while (true) {
    // Find the nearest enemy and the distance to it.
    var enemy = hero.findNearestEnemy();
    
    // If the enemy's type is "brawler"
    // AND the distance to it is less than 50 meters,
    // Then say "Fire!" to signal the artillery.
    if (enemy.type == "brawler" && hero.distanceTo(enemy) < 50)
        hero.say("Fire!");
}
