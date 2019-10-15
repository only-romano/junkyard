def sumHealth(enemies):
    totalHealth = 0
    for enemy in enemies:
        totalHealth += enemy.health
    return totalHealth

cannon = hero.findNearest(hero.findFriends())
enemies = cannon.findEnemies()
ogreSummaryHealth = sumHealth(enemies)
hero.say("Use " + ogreSummaryHealth + " grams.")
