def findStrongestEnemy(enemies):
    strongest = None
    strongestHealth = 0
    for enemy in enemies:
        if enemy.health > strongestHealth:
            strongest = enemy
            strongestHealth = enemy.health
    return strongest


leader = findStrongestEnemy(hero.findEnemies())
if leader:
    hero.say(leader)
