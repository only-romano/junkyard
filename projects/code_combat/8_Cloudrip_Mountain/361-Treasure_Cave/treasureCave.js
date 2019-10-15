// That ogre was defeated instantly! Better just avoid that yeti.

// We've hacked your fire-traps to go off after 5 seconds.
// The clearing to the north would be a good place for an explosive distraction.
// The yeti won't stay distracted forever, so hurry and grab the coins!
// After that run to the camp!
hero.buildXY("fire-trap", 64, 44);

while (hero.pos.y > 10) {
    hero.move({"x": 71, "y": 10});
}

while (hero.pos.x > 42) {
    hero.move({"x": 42, "y": 12});
}

var coin = hero.findNearestItem();

while (coin) {
    hero.move(coin.pos);
    coin = hero.findNearestItem();
}

while (hero.pos.x < 68) {
    hero.move({"x": 68, "y": 12});
}
