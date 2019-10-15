defendPoints = [{"x": 35, "y": 63},{"x": 61, "y": 63},{"x": 32, "y": 26},{"x": 64, "y": 26}];
summonTypes = ["soldier","soldier","soldier","soldier","archer","archer","archer","archer"];


def summonTroops():
    type = summonTypes[hero.built.length % summonTypes.length]
    if hero.gold >= hero.costOf(type):
        hero.summon(type)


def commandTroops():
    friends = hero.findFriends()
    for i in range(len(friends)):
        hero.command(friends[i], "defend", defendPoints[i % len(defendPoints)])


while True:
    summonTroops()
    commandTroops()
    if hero.canCast("regen") or hero.canCast("grow"):
        friends = hero.findFriends()
        heal = None
        minHP = 9000
        for i in range(len(friends)):""
            if friends[i].health < minHP:
                heal = friends[i]
                minHP = friends[i].health
        if heal:
            if hero.canCast("regen"):
                hero.cast("regen", heal)
            else:
                hero.cast("grow", heal)
