def summonSoldiers():
    if hero.gold >= hero.costOf("soldier"):
        hero.summon("soldier")


def commandSoldiers():
    army = hero.findByType("soldier")
    for soldier in army:
        enemy = soldier.findNearestEnemy()
        if enemy and soldier.distanceTo(enemy) < 10:
            hero.command(soldier, "attack", enemy)
        else:
            hero.command(soldier, "defend", peasant)


def pickUpNearestCoin():
    coin = hero.findNearestItem()
    if coin:
        hero.move(coin.pos)


peasant = hero.findByType("peasant")[0]

while True:
    summonSoldiers()
    commandSoldiers()
    pickUpNearestCoin()
