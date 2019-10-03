// Protect brandy from incoming thirsty yaks!
// Gather gold to build decoys to distract the yaks.
// Use flags to decide when and where to build decoys.
function flagFunc(flag) {
    var pos = flag.pos;
    if (hero.gold >= 25)
        hero.buildXY("decoy", pos.x, pos.y);
    hero.pickUpFlag(flag);
}

while (true) {
    var flag = hero.findFlag();
    if (flag)
        flagFunc(flag);
    var item = hero.findNearestItem();
    if (item) {
        hero.moveXY(item.pos.x, item.pos.y);
    }
}
