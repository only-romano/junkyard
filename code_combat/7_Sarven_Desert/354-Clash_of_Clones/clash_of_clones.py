def onlyFlag():
    flag = hero.findFlag()
    if flag:
        if hero.isReady("jump"):
            hero.jumpTo(flag.pos)
        hero.pickUpFlag(flag)


def summonIt():
    if hero.canCast("summon-burl"):
        hero.cast("summon-burl")
    if hero.canCast("summon-undead"):
        hero.cast("summon-undead")
    if hero.canCast("raise-dead") and len(hero.findCorpses()):
        hero.cast("raise-dead")


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


def battleTactics():
    onlyFlag()
    summonIt()

    enemy = hero.findNearestEnemy()
    if enemy and enemy.type != "sand-yak":
        attackIt(enemy)

    if hero.health < hero.maxHealth / 2:
        drainFriend()
            

while True:
    battleTactics()
