while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        enemyPos = enemy.pos.x + " " + enemy.pos.y
        hero.say("Enemy at " + enemyPos)

    item = hero.findNearestItem()
    if item:
        itemPos = item.pos.x + " " + item.pos.y
        hero.say("Item at " + itemPos)
