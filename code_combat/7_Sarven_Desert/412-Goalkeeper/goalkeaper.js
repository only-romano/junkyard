// Command the peasants to prevent the ogres from scoring.
// The fireball is type "ball".

var peasants = hero.findByType("peasant");
var fireball = hero.findByType("ball")[0];
while (true) {
    hero.command(peasants[0], "move", {x: peasants[0].pos.x, y: fireball.pos.y + 1});
    if (hero.time > 30 && hero.time < 32)
    hero.command(peasants[1], "move", {x: peasants[1].pos.x, y: fireball.pos.y - 5});
    else
    hero.command(peasants[1], "move", {x: peasants[1].pos.x, y: fireball.pos.y - 1});
    if (hero.canCast("haste"))
        hero.cast("haste", peasants[0]);
}
