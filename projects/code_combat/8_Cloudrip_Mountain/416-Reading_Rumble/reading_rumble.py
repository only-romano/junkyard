while True:
    enemy = hero.findNearestEnemy()
    if enemy and enemy.type == "brawler":
        hero.say(enemy.id.toUpperCase())
    elif enemy:
        hero.attack(enemy)
