def toBinary(num):
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    while len(binary) < 8:
        binary = "0" + binary
    return binary


def toTrinary(num):
    trinary = ""
    while num > 0:
        trinary = str(num % 3) + trinary
        num = num // 3
    while len(trinary) < 8:
        trinary = "0" + trinary
    return trinary


def numToUnits(order):
    units = []
    for i in range(len(order)):
        if (order[i] == "0")
            units.push("soldier")
        else if (order[i] == "1")
            units.push("archer")
        else if (order[i] == "2")
            units.push("griffin-rider")
    return units


def summonUnits(commander, binary):
    if binary:
        order = toBinary(commander.deployment)
    else:
        order = toTrinary(commander.deployment)

    units = numToUnits(order)
    for un in units:
        hero.summon(un);
        unit = hero.built[hero.built.length - 1]
        hero.command(unit, "move", {x: commander.pos.x + 8 + i * 5, y: commander.pos.y})


paladins = hero.findByType("paladin")
warlocks = hero.findByType("warlock")

for paladin in paladins:
    summonUnits(paladin, True)

for warlock in warlocks:
    summonUnits(warlocks[i], False)
