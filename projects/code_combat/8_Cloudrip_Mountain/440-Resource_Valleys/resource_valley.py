def commandPeasant(peasant, coins):
    coin = peasant.findNearest(coins)
    if coin:
        hero.command(peasant, "move", coin.pos)


friends = hero.findFriends()
peasants = {
    "Aurum": friends[0],
    "Argentum":friends[1],
    "Cuprum":friends[2]
}

while True:
    items = hero.findItems()
    goldCoins = [];
    silverCoins = [];
    bronzeCoins = [];
    for item in items:
        if item.value == 3:
            goldCoins.push(item)
        elif item.value == 2:
            silverCoins.push(item)
        elif item.value == 1:
            bronzeCoins.push(item)
    commandPeasant(peasants.Aurum, goldCoins)
    commandPeasant(peasants.Argentum, silverCoins)
    commandPeasant(peasants.Cuprum, bronzeCoins)
