// Lure the ogres into an ambush!

// While your gold is less than 25, collect coins.
while (hero.gold < 25) {
    var coin = hero.findNearestItem();
    if (coin) {
        hero.moveXY(coin.pos.x, coin.pos.y);
    }
}
// After the while loop, build a "decoy" at the white X.
hero.buildXY("decoy", 72, 68);
// While your health equals maxHealth, say insults
while (hero.health == hero.maxHealth) {
    hero.say("Coco");
}
// Then move back to the red X.
hero.moveXY(22, 15);
