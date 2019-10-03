function enemyDeal(target) {
    switch (target.type) {
        case "brawler":
            hero.cast("shrink", target);
            break;
        case "scout":
            hero.cast("poison-cloud", target);
            break;
        default:
            hero.cast("force-bolt", target);
    }
}

function friendDeal(target) {
    switch (target.type) {
        case "goliath":
            hero.cast("grow", target);
            break;
        case "soldier":
            hero.cast("heal", target);
            break;
        default:
            hero.cast("regen", target);
    }
}


function itemDeal(target) {
    if (target.type == "poison") {
        hero.cast("grow", hero);
        hero.cast("regen", hero);
    }
    hero.moveXY(target.pos.x, target.pos.y);
}


function doSome(x, y) {
    hero.moveXY(x, y);
    var target = hero.findNearestEnemy();
    if (target)
        enemyDeal(target);
    else {
        target = hero.findNearestFriend();
        if (target)
            friendDeal(target);
        else
            itemDeal(hero.findNearestItem());
    }
}


for (var i = 0; i < 4; i++) {
    var x = 18 + i * 16;
    doSome(x, 24);
    doSome(x, 40);
}
