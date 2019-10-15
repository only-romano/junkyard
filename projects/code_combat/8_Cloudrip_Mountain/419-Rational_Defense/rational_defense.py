def hideUnits(units):
    for i in range(len(units)):
        hero.command(units[i], "move", {x: 34, y: 10 + i * 12})


peasants = hero.findFriends()
types = peasants[0].buildOrder.split(",")

for i in range(len(peasants)):
    hero.command(peasants[i], "buildXY", types[i], 16, 10 + i * 12)

while True:
    if hero.findNearestEnemy():
        hideUnits(peasants)
        break

while True:
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 45:
        hero.attack(enemy)
