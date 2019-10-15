def onlyFlag():
    flag = hero.findFlag()
    if flag:
        if hero.isReady("jump"):
            hero.jumpTo(flag.pos)
        else:
            hero.moveXY(flag.pos.x, flag.pos.y)
        hero.pickUpFlag(flag)


def summonIt():
    if hero.canCast("summon-burl"):
        hero.cast("summon-burl")
    if hero.canCast("summon-undead"):
        hero.cast("summon-undead")
    if hero.canCast("raise-dead") and len(hero.findCorpses()):
        hero.cast("raise-dead")


def summonArmy():
    gold = hero.gold
    if gold > hero.costOf("soldier"):
        hero.summon("soldier")

    army = hero.findFriends()
    for soldier in army:
        if soldier.type == "soldier":
            enemy = soldier.findNearestEnemy()
            if enemy:
                hero.command(soldier, "attack", enemy)


def attackIt(enemy):
    distance = hero.distanceTo(enemy)
    if distance < 25 and hero.canCast("fear"):
        hero.cast("fear", enemy)
    elif distance < 30 and hero.canCast("chain-lightning"):
        hero.cast("chain-lightning", enemy)
    elif distance < 30 and hero.canCast("poison-cloud"):
        hero.cast("poison-cloud", enemy)
    elif distance < 15 and hero.health < hero.maxHealth / 1.5:
        hero.cast("drain-life", enemy)
    else:
        hero.attack(enemy)


def drainFriend():
    friend = hero.findNearest(hero.findFriends())
    if friend and friend.type != "burl" and hero.distanceTo(friend) <= 15:
        hero.cast("drain-life", friend)


def getBestCoin():
    coins = hero.findItems()
    best = None
    value = 0
    for coin in coins:
        now = coin.value / hero.distanceTo(coin)
        if now > value:
            value = now
            best = coin
    return best


def battleTactics():
    onlyFlag()
    summonIt()
    
    coin = getBestCoin()
    if coin:
        hero.move(coin.pos)

    summonArmy()
    enemy = hero.findNearestEnemy()
    if enemy:
        attackIt(enemy)

    if hero.health < hero.maxHealth / 2:
        drainFriend()
            

while True:
    battleTactics()
