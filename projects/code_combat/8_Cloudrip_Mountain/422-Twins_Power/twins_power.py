def areTwins(unit1, unit2):
    name1 = unit1.id
    name2 = unit2.id
    if len(name1) != len(name2):
        return False
    for i in range(len(name1)):
        if name1[i] != name2[i]:
            return False
    return True


paladins = hero.findByType("paladin")
for i in range(len(paladins)):
    for j in range(len(paladins)):
        if i == j:
            continue;
        if areTwins(paladins[i], paladins[j]):
            hero.say(paladins[i].id + " " + paladins[j].id)

hero.moveXY(65, 36)
hero.moveXY(13, 36)
