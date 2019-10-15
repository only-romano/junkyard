// Get to the Oasis by moving down 10m at a time.
// Build fences 20m to the left of each ogre.
var pos = {x: hero.pos.x, y: hero.pos.y};
while(true) {
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        // buildXY a "fence" 20 meters to enemy's left.
        hero.buildXY("fire-trap", enemy.pos.x - 15, enemy.pos.y);
    }
    pos.y = pos.y - 10;
    hero.moveXY(pos.x, pos.y);
}
