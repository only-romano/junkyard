def sumHealth(units):
    totalHealth = 0
    for unit in units:
        totalHealth += unit.health

    return totalHealth


while True:
    if sumHealth(hero.findFriends()) <= sumHealth(hero.findEnemies()):
        hero.say("Wait")
    else
        hero.say("ATTACK!!!")
