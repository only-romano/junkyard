def pickUpNearestCoin():
    nearestCoin = hero.findNearest(hero.findItems())
    if nearestCoin:
        hero.move(nearestCoin.pos)


def summonSoldier():
    if hero.gold > hero.costOf("soldier"):
        hero.summon("soldier")


def commandSoldiers():
    friends = hero.findFriends()
    for friend in friends:
        enemy = friend.findNearestEnemy()
        if enemy and friend.type == "soldier":
            hero.command(friend,"attack", enemy)


def summonIt():
    if hero.canCast("summon-burl"):
        hero.cast("summon-burl")
    if hero.canCast("summon-undead"):
        hero.cast("summon-undead")
    if hero.canCast("raise-dead") and hero.findCorpses().length:
        hero.cast("raise-dead")

while True:
    pickUpNearestCoin()
    summonSoldier()
    commandSoldiers()
    summonIt()
