// To disable the fire-traps add the lowest trap.value to the highest value.
// Move to the white X and say the answer to Kitty the cougar.
// Defeat all the ogres if you dare.
// Once all ogres are defeated move to the red X.
// Look out for potions to boost your health.

function onSpawn() {
    var item = hero.findNearestItem();
    if (item)
        pet.fetch(item);
}

var whiteX = {x:27, y:42};
var redX = {x:151 , y: 118};
pet.on("spawn", onSpawn);

var traps = hero.findHazards();
var max = 0;
var min = 9999;

for (var i = 0; i < traps.length; i++) {
    var value = traps[i].value;
    if (value) {
        if (value < min)
            min = value;
        if (value > max)
            max = value;
    }
}

hero.moveXY(whiteX.x, whiteX.y);
hero.say(min + max);
hero.moveXY(redX);
