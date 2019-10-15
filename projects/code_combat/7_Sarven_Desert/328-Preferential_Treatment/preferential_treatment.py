enemies = hero.findEnemies()

for enemy in enemies:
    if enemy and enemy.type == "thrower":
        hero.attack(enemy)

enemies = hero.findEnemies()

for enemy in enemies:
    if hero.isReady("bash"):
        hero.bash(enemy)
    else:
        hero.attack(enemy)
