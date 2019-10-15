// Use "if" and "else if" to handle any situation.
// Put it all together to defeat enemies and pick up coins!
// Make sure you bought great armor from the item shop! 400 health recommended.

while(true) {
    var flag = hero.findFlag();
    var enemy = hero.findNearestEnemy();
    var item = hero.findNearestItem();

    if (flag) {
        // What happens when I find a flag?
        hero.moveXY(flag.pos.x, flag.pos.y);
        hero.pickUpFlag(flag);
    }
    else if (enemy) {
        // What happens when I find an enemy?
        if (hero.canCast("drain-life")) {
            hero.cast("drain-life", enemy);
        } else if (hero.canCast("chain-lightning")) {
            hero.cast("chain-lightning", enemy);
        } else {
            hero.attack(enemy);
        }
    }
    else if (item) {
        // What happens when I find an item?
        if (item.type !== "poison") {
            hero.moveXY(item.pos.x, item.pos.y);
        }
    }
}
