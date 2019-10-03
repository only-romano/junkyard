// Grab all the coins and use flags to build traps behind
// you to deal with those ogres.

while(true) {
    var flag = hero.findFlag();
    var item = hero.findNearestItem();
    if (flag) {
        var pos = flag.pos;
        hero.pickUpFlag(flag);
        hero.buildXY("fire-trap", pos.x, pos.y);
    }
    if (item) {
        hero.moveXY(item.pos.x, item.pos.y);
        continue;
    }
}
