// Recruit soldiers and archers to fill out each squadron.
// Each paladin has a decimal number stored in her deployment attribute.
// Convert these to binary and represent them with lines of soldiers and archers next to each paladin.
// Soldiers are 0s, archers are 1s.
// For the bonus goal, add griffins as 2s for trinary number lines next to the warlocks.
// Check the guide for help with binary numbers.

function toBinary(num) {
    var binary = "";
    while (num > 0) {
        binary = (num % 2) + binary;
        num = Math.floor(num / 2);
    }
    while (binary.length < 8)
        binary = "0" + binary;
    return binary;
}

function toTrinary(num) {
    var trinary = "";
    while (num > 0) {
        trinary = (num % 3) + trinary;
        num = Math.floor(num / 3);
    }
    while (trinary.length < 8)
        trinary = "0" + trinary;
    return trinary;
}

function numToUnits(order) {
    var units = [];
    for (var i = 0; i < order.length; i++) {
        if (order[i] == "0")
            units.push("soldier");
        else if (order[i] == "1")
            units.push("archer");
        else if (order[i] == "2")
            units.push("griffin-rider");
    }
    return units;
}

function summonUnits(commander, binary) {
    var order;
    if (binary)
        order = toBinary(commander.deployment);
    else
        order = toTrinary(commander.deployment);

    var units = numToUnits(order);
    for (var i = 0; i < units.length; i++) {
        hero.summon(units[i]);
        var soldier = hero.built[hero.built.length - 1];
        hero.command(soldier, "move", {x: commander.pos.x + 8 + i * 5, y: commander.pos.y});
    }
}

var paladins = hero.findByType("paladin");
var warlocks = hero.findByType("warlock");

for (var i = 0; i < paladins.length; i++)
    summonUnits(paladins[i], true);

for (i = 0; i < warlocks.length; i++)
    summonUnits(warlocks[i], false);
