summonTypes = False

def summonTroops():
    typeTo = "soldier"
    if summonTypes:
        typeTo = "archer"
    if hero.gold >= hero.costOf(typeTo):
        hero.summon(typeTo)
        summonTypes = not summonTypes


def commandAll():
    friends = hero.findFriends()
    for friend in friends:
        if friend.type == "archer" or friend.type == "soldier":
            enemy = friend.findNearestEnemy()
            if enemy:
                hero.command(friend, "attack", enemy)


def collectGold():
    coin = hero.findNearestItem()
    if coin:
        hero.move(coin.pos)


while True:
    collectGold()
    summonTroops()
    commandAll()
