// The pos property is an object with x and y properties.
// pos.x is a number representing the horizontal position on the map
// pos.y is a number representing the vertical position on the map

while(true) {
    var enemy = hero.findNearestEnemy();
    if(enemy) {
        var x = enemy.pos.x;
        // Get the enemy's y position!
        var y = enemy.pos.y; // ∆ Change this!

        // say the x and y position separated by a comma
        hero.say(x + ',' + y);
    } else {
        hero.say("Cease" + " " + "Fire!");
    }
}
