def attackIt():
    while True:
        flag = hero.findFlag()
        if flag:
            if flag.color == "green":
                break;
            if hero.isReady("jump"):
                hero.jumpTo(flag.pos)
            hero.pickUpFlag(flag)
    
        if hero.canCast("summon-burl"):
            hero.cast("summon-burl");
        if hero.canCast("summon-undead"):
            hero.cast("summon-undead");
        if hero.canCast("raise-dead"):
            hero.cast("raise-dead");
    
        enemy = hero.findNearestEnemy()
        if enemy and enemy.type != "sand-yak":
            distance = hero.distanceTo(enemy)
            if distance < 25 and hero.canCast("fear"):
                hero.cast("fear", enemy)
            elif distance < 30 and hero.canCast("chain-lightning"):
                hero.cast("chain-lightning", enemy)
            elif distance < 30 and hero.canCast("poison-cloud"):
                hero.cast("poison-cloud", enemy)
            elif distance < 15 and hero.canCast("drain-life"):
                hero.cast("drain-life", enemy)
            else:
                hero.attack(enemy)
            
        if hero.health < hero.maxHealth / 2:
            friend = hero.findNearest(hero.findFriends())
            if friend and friend.type != "burl" and hero.distanceTo(friend) <= 15:
                hero.cast("drain-life", friend)

while True:
    flag = hero.findFlag()
    if flag:
        if flag.color == "black":
            hero.pickUpFlag(flag)
            attackIt()
        else:
            hero.pickUpFlag(flag)
