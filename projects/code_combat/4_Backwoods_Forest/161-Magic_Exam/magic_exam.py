def enemyDeal(target):
    if target.type == "brawler":
        hero.cast("shrink", target)
    elif target.type == "scout":
        hero.cast("poison-cloud", target)
    else:
        hero.cast("force-bolt", target)


def friendDeal(target):
    if target.type == "goliath":
        hero.cast("grow", target)
    elif target.type == "soldier":
        hero.cast("heal", target)
    else:
        hero.cast("regen", target)


def itemDeal(target):
    if target.type == "poison":
        hero.cast("grow", hero)
        hero.cast("regen", hero)
    hero.moveXY(target.pos.x, target.pos.y)


def doSome(x, y):
    hero.moveXY(x, y)
    target = hero.findNearestEnemy()
    if target:
        enemyDeal(target)
    else:
        target = hero.findNearestFriend()
        if target:
            friendDeal(target)
        else:
            itemDeal(hero.findNearestItem())


for i in range(4):
    x = 18 + i * 16
    doSome(x, 24)
    doSome(x, 40)
