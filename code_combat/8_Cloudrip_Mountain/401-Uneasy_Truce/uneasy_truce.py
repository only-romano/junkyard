def findSouthernUnits(units):
    southernUnits = []
    for unit in units:
        if unit.pos.y < hero.pos.y:
            southernUnits.append(unit)
    return southernUnits


while True:
    if len(findSouthernUnits(hero.findEnemies())) > len(hero.findFriends()):
        hero.summon("soldier")
