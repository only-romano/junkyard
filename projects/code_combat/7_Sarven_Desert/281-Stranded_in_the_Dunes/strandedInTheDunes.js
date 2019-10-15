// Go to the far right edge of the level to find new areas.
// Check the guide for more details.

function onSpawn() {
    while (true) {
        var item = hero.findNearestItem();
        if (item) {
            pet.fetch(item);
        }
    }
}

function goToFlag(flag) {
    hero.move(flag.pos);
    hero.pickUpFlag(flag);
}

function surviveYak(enemy) {
    var pos = hero.pos;
    var y = pos.y;
    var enY = enemy.pos.y;
    if (enY >= y) {
        if (hero.isPathClear(pos, {x: pos.x, y: y - 12}))
            y -= 12;
        else
            y += 12;
    } else {
        if (hero.isPathClear(pos, {x: pos.x, y: y + 12}))
            y += 12;
        else
            y -= 12;
    }
    hero.moveXY(pos.x, y);
}

hero.moveXY(119, 31);
pet.on("spawn", onSpawn);

while (true) {
    var flag = hero.findFlag();
    if (flag)
        goToFlag(flag);

    var enemy = hero.findNearestEnemy();
    if (enemy && enemy.type == "sand-yak") {
        surviveYak(enemy);
    } else if (enemy) {
        if (hero.isReady("cleave"))
            hero.cleave(enemy);
        else if (hero.isReady("bash"))
            hero.bash(enemy);
        else
            hero.attack(enemy);
    }

}

