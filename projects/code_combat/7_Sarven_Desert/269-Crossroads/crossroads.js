// Use "fire-trap"s to defeat the ogres.

while(true) {
    var enemy = hero.findNearestEnemy();
    if(enemy) {
        // If the enemy is to the left of the hero:
        if(enemy.pos.x < hero.pos.x) {
            // buildXY a "fire-trap" on the left X.
            hero.buildXY("fire-trap", 25, 34);
        // If the enemy is to the right of the hero:
        } else if (enemy.pos.x > hero.pos.x) {
            // buildXY a "fire-trap" on the right X.
            hero.buildXY("fire-trap", 55, 34);
            
        // If the enemy is below the hero:
        } else if (enemy.pos.y < hero.pos.y) {
            // buildXY a "fire-trap" on the bottom X.
            hero.buildXY("fire-trap", 40, 19);
            
        // If the enemy is above the hero:
        } else if (enemy.pos.y > hero.pos.y) {
            // buildXY a "fire-trap" on the top X.
            hero.buildXY("fire-trap", 40, 49);
            
        }
    }
    // Move back to the center.
    hero.moveXY(40, 34);
}
