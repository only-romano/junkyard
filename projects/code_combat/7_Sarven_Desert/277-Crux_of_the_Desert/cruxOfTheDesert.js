// Figure out which direction the ogres are coming from.

while(true) {
    var enemy = hero.findNearestEnemy();
    if(enemy) {
        // Left: enemy.pos.x is less than hero.pos.x
        var isLeft = hero.pos.x  > enemy.pos.x;
        // Above: enemy.pos.y is greater than hero.pos.y
        var isAbove = hero.pos.y < enemy.pos.y;
        // Right: enemy.pos.x is greater than hero.pos.x
        var isRight = enemy.pos.x > hero.pos.x;
        // Below: enemy.pos.y is less than hero.pos.y
        var isBelow = enemy.pos.y < hero.pos.y;
        // If enemy isAbove and isLeft:
        // buildXY() a "fire-trap" at the X mark.
        if(isLeft && isAbove) {
            hero.buildXY("fire-trap", 20, 51);
        }
        // If enemy isAbove and isRight:
        // buildXY() a "fire-trap" at the X mark.
        if (isAbove && isRight)
            hero.buildXY("fire-trap", 60, 51);
        // If enemy isBelow and isLeft:
        // buildXY() a "fire-trap" at the X mark.
        if (isAbove && isLeft)
            hero.buildXY("fire-trap", 20, 51);
        if (isBelow && isLeft)
            hero.buildXY("fire-trap", 20, 17);
        
        // If enemy isBelow and isRight:
        // buildXY() a "fire-trap" at the X mark.
        if (isBelow && isRight)
            hero.buildXY("fire-trap", 60, 17);
        
        hero.moveXY(40, 34);
    } else {
        hero.moveXY(40, 34);
    }
}
