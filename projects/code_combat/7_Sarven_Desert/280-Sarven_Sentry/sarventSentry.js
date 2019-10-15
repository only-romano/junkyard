// Use different colored flags to perform different tasks.

while(true) {
    var flagGreen = hero.findFlag("green");
    var flagBlack = hero.findFlag("black");
    
    // If there's a flagGreen...
    if (flagGreen) {
        // Build a "fence" at flagGreen's position.
        var pos = flagGreen.pos;
        hero.buildXY("fence", pos.x, pos.y);
        // Pick up the flag!
        hero.pickUpFlag(flagGreen);
    }
    // If there's a flagBlack...
    if (flagBlack) {
        // Build a "fire-trap" at flagBlack's position.
        var pos = flagBlack.pos;
        hero.buildXY("fire-trap", pos.x, pos.y);
        // Pick up the flag!
        hero.pickUpFlag(flagBlack);
    }
    // Move back to the center.
    hero.moveXY(43, 31);
}
