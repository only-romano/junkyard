from math import pi, sin, cos

def commandSoldier(soldier, soldierIndex, numSoldiers):
    angle = pi * 2 * soldierIndex / numSoldiers
    defendPos = {x: 41, y: 40}
    defendPos.x += 10 * cos(angle)
    defendPos.y += 10 * sin(angle)
    hero.command(soldier, "defend", defendPos)


def findStrongestTarget():
    mostHealth = 0
    bestTarget = None
    enemies = hero.findEnemies()
    for enemy in enemies:
        if enemy.health > mostHealth:
            bestTarget = enemy
            mostHealth = enemy.health
    if bestTarget and bestTarget.health > 15:
        return bestTarget
    else:
        return None


def commandArcher(archer):
    nearest = archer.findNearestEnemy()
    if archerTarget:
        hero.command(archer, "attack", archerTarget)
    elif nearest:
        hero.command(archer, "attack", nearest)


archerTarget = None
while True:
    if not archerTarget or archerTarget.health <= 0:
        archerTarget = findStrongestTarget()
    friends = hero.findFriends()
    soldiers = hero.findByType("soldier")
    archers = hero.findByType("archer")
    for soldier in soldiers:
        commandSoldier(soldier, i, soldiers.length)
    for archer in archers:
        commandArcher(archer)
