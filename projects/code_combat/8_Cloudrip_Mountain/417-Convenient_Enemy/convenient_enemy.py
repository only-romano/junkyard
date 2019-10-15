for x in range(8, 73, 16):
    hero.moveXY(x, 22)
    peasant = hero.findNearest(hero.findFriends())
    message = peasant.message
    if message:
        words = message.split(" ")
        unit = words[-1]
        hero.summon(unit)

for i in range(len(hero.built)):
    unit = hero.built[i]
    hero.command(unit, "defend", unit.pos)


while True:
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 45:
        hero.attack(enemy)
