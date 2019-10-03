// You can find friends through walls, but not enemies.
// Watch out for smooth, frictionless ice patches!

function moveTo(position, fast) {
    if (hero.isReady("jump") && fast)
        hero.jumpTo(position);
    else
        hero.move(position);
}


function commandTroops() {
    var friends = hero.findFriends();
    for (var i = 0; i < friends.length; i++) {
        var friend = friends[i];
        var enemies = hero.findEnemies();
        var witch = hero.findNearest(hero.findByType('witch'));
        if (enemies.length > 0 && witch) {
            if (friend.type == 'paladin')
                CommandPaladin(friend);
            else
                CommandSoldier(friend);
        }
        else if (hero.now() < 10 && hero.now() > 5 && friend.type == 'paladin') {
            if (friend.canCast("heal"))
                hero.command(friend, "cast", "heal", friend);
            else if (hero.now() < 7)
                hero.command(friend, "move", {'x': 31, 'y': 40});
            else if (hero.now() < 12)
                hero.command(friend, "move", {'x': 7, 'y': 40});
        }
        else if (hero.now() < 15 && friend.type != 'archer') {
            var worst = findWorstEnemy();
            if (worst && friend.pos.x - worst.pos.x < 10)
                hero.command(friend, "move", {'x': 50, 'y': 58});
        }
        else if (friend.type == 'archer' && hero.now() < 15) {
            if (hero.now() < 7)
                hero.command(friend, "move", {'x': 6, 'y': 58});
            else
                hero.command(friend, "move", {'x': 49, 'y': 58});
        }
        else if (hero.now() < 17)
            hero.command(friend, "move", {'x': 50, 'y': 39});
        else
            hero.command(friend, "move", {'x': 78, 'y': 40});
    }
}


function CommandPaladin(paladin) {
    var target;
    if (paladin.canCast("heal")) {
        target = lowestHealthFriend();
        if (target)
            hero.command(paladin, "cast", "heal", target);
    }
    else if (paladin.health < 100)
        hero.command(paladin, "shield");
    else {
        target = findWorstEnemy();
        if (target)
            hero.command(paladin, "attack", target);
    }
}


function CommandSoldier(soldier) {
    var target = findWorstEnemy();
    if (target)
        hero.command(soldier, "attack", target);
}


function findWorstEnemy() {
    var witch = hero.findNearest(hero.findByType('witch'));
    var ogre = hero.findNearest(hero.findByType('ogre'));
    var skeleton = hero.findNearest(hero.findByType('skeleton'));
    if (witch)
        return witch;
    else if (ogre)
        return ogre;
    else if (skeleton)
        return skeleton;
    else
        return null;
}


function lowestHealthFriend() {
    var lowestHealth = 99999;
    var lowestFriend = null;
    var friends = hero.findFriends();
    for (var i = 0; i < friends.length; i++) {
        var friend = friends[i];
        if (friend.health < lowestHealth && friend.health < friend.maxHealth) {
            lowestHealth = friend.health;
            lowestFriend = friend;
        }
    }
    return lowestFriend;
}


function attack(target) {
    if (target) {
        if (hero.distanceTo(target) > 10)
            moveTo(target.pos, true);
        else if (hero.isReady("bash"))
            hero.bash(target);
        else
            hero.attack(target);
    }
}


while (true) {
    commandTroops();
    var brawler = hero.findNearest(hero.findByType('brawler'));
    var catapult = hero.findNearest(hero.findByType('catapult'));
    if (brawler && hero.distanceTo(brawler) > 15)
        moveTo(brawler.pos, false);
    else if (brawler) {
        var runaway = Vector.subtract(hero.pos, brawler.pos);
        runaway = Vector.normalize(runaway);
        runaway = Vector.multiply(runaway, 15);
        var direction = Vector.add(runaway, hero.pos);
        moveTo(direction, false);
    }
    else if (catapult)
        attack(catapult);
    else
        hero.move({'x': 78, 'y': 15});
}
