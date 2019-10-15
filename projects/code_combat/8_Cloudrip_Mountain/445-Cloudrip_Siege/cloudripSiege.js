// Your goal is to keep at least one flower alive for 60 seconds.
// This is an optional challenge level, intended to be difficult. Be creative with your code!
// It gets harder (and more lucrative) each time you succeed. If you fail, you must wait a day to resubmit.

function moveTo(item) {
    if (hero.isReady("jump") && hero.distanceTo(item) > 10)
        hero.jumpTo(item.pos);
    else
        hero.move(item.pos);
}


function pickUpNearestItem() {
    var item = hero.findNearestItem();
    if (item)
        moveTo(item);
}


var coords = [[67, 41], [24, 54], [69, 55], [25, 34], [69, 32]];
var buildTypes = ['arrow-tower'];


function buildTroops() {
    coord = coords[len(hero.built) % len(coords)]
    if hero.gold > hero.costOf('arrow-tower'):
        hero.buildXY('arrow-tower', coord[0], coord[1])
}


while (true) {
    pickUpNearestItem();
    buildTroops();
}
