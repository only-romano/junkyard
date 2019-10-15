// Use flags to tell your players where to ram the ball.
// Use removeFlag when a player gets close to a flag.

function onFlag(flag, peasants) {
    var nearest = null;
    var distance = 1000;
    for (var i = 0; i < peasants.length; i++) {
        if (peasants[i].distanceTo(flag) < distance) {
            nearest = peasants[i];
            distance = peasants[i].distanceTo(flag);
        }
    }
    if (nearest) {
        hero.command(nearest, "move", flag.pos);
        if (nearest.distanceTo(flag) < 4)
            hero.removeFlag(flag);
    }

    for (i = 0; i < peasants.length; i++) {
        if (peasants[i] == nearest)
            continue;
        hero.command(peasants[i], "move", pos[i]);
    }
}

var peasants = hero.findByType("peasant");
var pos = [];
pos.push(peasants[0].pos);
pos.push(peasants[1].pos);
pos.push(peasants[2].pos);

while (true) {
    var flag = hero.findFlag();
    if (flag) {
        onFlag(flag, peasants);
    }
}
