// What eldritch artifacts are these? Don't let them blast you!
// The ice gate will open when both ogres are defeated.
// What eldritch artifacts are these? Don't let them blast you!
// The ice gate will open when both ogres are defeated.

var excepE = ['tower'];
var dest = {'x': 78, 'y': 39};
var done = false;


function selfDying(one) {
    if (one.health < one.maxHealth / 2)
        hero.command(one, "move", {'x': one.pos.x - 1, 'y': one.pos.y});
}


function evade() {
    var x = hero.pos.x;
    var y = hero.pos.y;
    var orbs = hero.findEnemyMissiles();
    if (orbs.length) {
        var orb = hero.findNearest(orbs);
        if (hero.distanceTo(orb) < 3) {
            if (y > 21) {
                hero.moveXY(x, y - 7);
            }
            else {
                hero.moveXY(x, y + 7);
            }
        }
    }
}


function lowHP() {
    var friends = hero.findFriends();
    var lowest = 9999;
    var dying = null;
    if (friends.length) {
        for (var i = 0; i < friends.length; i++) {
            var friend = friends[i];
            var hp = friend.health;
            if (hp < friend.maxHealth / 3 && hp < lowest && hp > 0) {
                lowest = hp;
                dying = friend;
            }
        }
    }
    return dying;
}


function soldierAtk(soldier) {
    selfDying(soldier);
    var enemies = hero.findByType("ogre");
    var enemy;
    if (!enemies.length)
        enemy = soldier.findNearestEnemy();
    else
        enemy = enemies[0];
    if (enemy)
        hero.command(soldier, "attack", enemy);
    else
        hero.command(soldier, "move", soldier.pos);
}


function archerAtk(archer) {
    var enemies = hero.findByType("chieftain");
    var enemy;
    if (!enemies.length)
        enemy = archer.findNearestEnemy();
    else
        enemy = enemies[0];
    if (enemy && archer.pos.x > 53 && archer.pos.y < 40)
        hero.command(archer, "attack", enemy);
    else if (hero.time > 6)
        hero.command(archer, "move", dest);
}


function riderAtk(rider) {
    var enemies = hero.findByType("robot-walker");
    if (enemies.length)
        hero.command(rider, "move", {'x': enemies[0].pos.x / 2 + enemies[1].pos.x / 2,
                                     'y': enemies[0].pos.y / 2 + enemies[1].pos.y / 2});
}


function palaAtk(pala) {
    selfDying(pala);
    var dying = lowHP();
    var enemies = hero.findByType("witch");
    var enemy;
    if (!enemies.length)
        enemy = pala.findNearestEnemy();
    else
        enemy = enemies[0];
    if (dying && pala.canCast('heal'))
        hero.command(pala, "cast", 'heal', dying);
    else
        hero.command(pala, "move", dest);
    if (pala.canCast('heal') && hero.health < 2 * hero.maxHealth / 3)
        hero.command(pala, "cast", 'heal', hero);
    if (pala.pos == dest)
        hero.command(pala, "shield");
}


function summon(soldier) {
    while (hero.gold >= hero.costOf(soldier))
        hero.summon(soldier);
}


function command() {
    var friends = hero.findFriends();
    for (var i = 0; i < friends.length; i++) {
        var unit = friends[i];
        var t = unit.type;
        if (t == 'griffin-rider')
            riderAtk(unit);
        else if (t == 'soldier')
            soldierAtk(unit);
        else if (t == 'paladin')
            palaAtk(unit);
        else if (t == 'archer')
            archerAtk(unit);
    }
}


function atk() {
    if (hero.gold > hero.costOf('griffin-rider'))
        hero.summon('griffin-rider');
    command();

    var enemies = hero.findByType("robot-walker");
    if (!enemies.length) {
        var nearest = hero.findEnemies();
        var can = [];
        for (var i = 0; i < nearest.length; i++) {
            if (nearest[i].type != "ice-yak" && nearest[i].type != "cow")
                can.push(nearest[i]);
        }
        var enemy = hero.findNearest(can);
        if (enemy) {
            command();
            if (hero.canCast("chain-lightning", enemy) && hero.time > 7)
                hero.cast("chain-lightning", enemy);
        }
        else if (!enemies.length)
            hero.move({'x': 78, 'y': 14});
    }
    return true;
}


function run() {
    while (true) {
        evade();
        atk();
    }
}


run();
