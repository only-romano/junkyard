while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.say(enemy.pos.x + ',' + enemy.pos.y);
    else:
        hero.say("Cease" + " " + "Fire!");
