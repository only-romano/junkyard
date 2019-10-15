def removeByType(enemies, excludedType):
    tempArray = []
    for enemy in enemies:
        if enemy.type != excludedType:
            tempArray.append(enemy)
    return tempArray


while True:
    enemy = hero.findNearest(removeByType(hero.findEnemies(), "sand-yak"))
    if enemy:
        hero.attack(enemy)
