# Defeat the enemy hero in two minutes.
def heal(enemy):
    if enemy and hero.distanceTo(enemy) < 15:
        hero.cast("drain-life", enemy)


def fear(enemies, enemy):
    if hero.canCast("fear") and len(enemies) and enemy and hero.distanceTo(enemy) < 25:
        hero.cast("fear", enemy)


def raiseDead(corpses):
    if hero.canCast("raise-dead") and len(corpses) > 3:
        nearest = hero.findNearest(corpses)
        if nearest:
            if hero.isReady("jump"):
                hero.jumpTo(nearest.pos)
            else:
                hero.move(nearest.pos)
            if hero.distanceTo(nearest) < 10:
                hero.cast("raise-dead")


def goldStorm():
    if hero.canCast("goldstorm"):
        hero.cast("goldstorm")


def findBest(coins):
    best = None
    cost = 0
    for coin in coins:
        value = coin.value / hero.distanceTo(coin)
        if value > cost:
            best = coin
            cost = value
    return best


def collectGold():
    coin = findBest(hero.findItems())
    if coin:
        hero.move(coin.pos)


def attackIt(enemy):
    if enemy and hero.distanceTo(enemy) < 40:
        hero.attack(enemy)


def summon(gold, index):
    units = ["soldier", "archer", "griffin-rider"]
    if hero.gold > hero.costOf(units[index]):
        hero.summon(units[index])
        index += 1
        if index == 3:
            index = 0
    return index


ind = 0
while True:
    enemies = hero.findEnemies()
    nearestEnemy = hero.findNearest(enemies)

    fear(enemies, nearestEnemy)
    attackIt(hero.findNearestEnemy())
    if hero.health < hero.maxHealth:
        heal(hero.findNearestEnemy())
    raiseDead(hero.findCorpses())

    
    # Your hero can collect coins and summon troops.
    ind = summon(hero.gold, ind)
    # She also commands your allies in battle.
    friends = hero.findFriends()
    for friend in friends:
        hero.command(friend, "attack", friend.findNearest(enemies))
    collectGold()
    # Use your hero's abilities to turn the tide.
    goldStorm()
    