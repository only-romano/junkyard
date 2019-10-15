while True:
    enemy = hero.findNearestEnemy()
    if enemy.type == "brawler" and hero.distanceTo(enemy) < 50:
        hero.say("Fire!")
