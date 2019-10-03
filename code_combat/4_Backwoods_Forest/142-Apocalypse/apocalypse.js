// The artillery apocalypse is upon us!
// Dodge the incoming shells for 60 seconds.
// Tip: flags might come in handy, like in Coinucopia.
// Because the attacks are random each time you submit, you can't hard-code moveXYs.
while (true) {
    var flag = hero.findFlag();
    if (flag) {
        hero.pickUpFlag(flag);
    }
}
