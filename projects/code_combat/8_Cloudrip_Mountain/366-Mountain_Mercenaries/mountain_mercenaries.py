while True:
    coin = hero.findNearestItem();
    if coin:
        hero.move(coin.pos)
    
    if hero.gold > hero.costOf("soldier"):
        hero.summon("soldier")

    enemy = hero.findNearest(hero.findEnemies())
    if enemy:
        soldiers = hero.findFriends()
        for soldier in soldiers:
            hero.command(soldier, "attack", enemy)
