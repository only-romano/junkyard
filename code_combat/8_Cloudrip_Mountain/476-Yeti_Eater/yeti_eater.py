wizard = hero.findNearest(hero.findFriends())
yetis = wizard.findEnemies()

for i in range(yetis.length - 1, -1, -1):
    enemy = yetis[i]
    while enemy and enemy.health > 0:
        hero.attack(enemy)
