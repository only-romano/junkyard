// Incoming oscars! (That's military speak for ogres).
// You will need to calculate their angle of attack.
// Use that angle to command your Griffin Bombers!

while(true) {
    var enemy = hero.findNearestEnemy();
    if(enemy && hero.distanceTo(enemy) < 60) {
        // Find the vector of attack
        var x = Math.abs(enemy.pos.x - hero.pos.x);
        var y = Math.abs(enemy.pos.y - hero.pos.y);
        // Use trigonometry to find the the angle in Radians!
        var angle = Math.atan2(y, x);
        // The answer must be in Degrees!
        // To convert Radians to Degrees multiply by (180 / Math.PI)
        angle = angle * 180 / Math.PI;
        if (enemy.pos.x < hero.pos.x)
            angle = 180 - angle;
        
        // Say the angle!
        hero.say(angle);
    }
}
