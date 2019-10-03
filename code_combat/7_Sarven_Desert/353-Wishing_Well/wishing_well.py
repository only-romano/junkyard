less = "Nimis";
more = "Non satis";
requiredGold = 104;

def sumCoinValues(coins):
    totalValue = 0;
    for coin in coins:
        totalValue += coin.value
    return totalValue


def collectAllCoins():
    item = hero.findNearest(hero.findItems())
    while item:
        hero.moveXY(item.pos.x, item.pos.y)
        item = hero.findNearest(hero.findItems())


while True:
    items = hero.findItems()
    goldAmount = sumCoinValues(items)
    if goldAmount != 0:
        if goldAmount < requiredGold:
            hero.say(less)
        elif goldAmount > requiredGold:
            hero.say(more)
        else:
            collectAllCoins()
