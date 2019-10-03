def lowestHealthPaladin():
    lowestHealth = 99999
    lowestFriend = None
    friends = hero.findFriends()
    for friend in friends:
        if friend.type != "paladin":
            continue
        if friend.health < lowestHealth and friend.health < friend.maxHealth:
            lowestHealth = friend.health
            lowestFriend = friend
    return lowestFriend


def commandPaladin(paladin):
    lowest = lowestHealthPaladin()
    enemy = paladin.findNearestEnemy()
    if paladin.canCast("heal") and lowest:
        hero.command(paladin, "cast", "heal", lowest)
    elif enemy and paladin.health > paladin.maxHealth * 0.5:
        hero.command(paladin, "attack", enemy)
    else:
        hero.command(paladin, "shield")


def commandFriends():
    friends = hero.findFriends()
    for friend in friends:
        if friend.type == "peasant":
            commandPeasant(friend)
        elif friend.type == "griffin-rider":
            commandGriffin(friend)
        elif friend.type == "paladin":
            commandPaladin(friend)


def commandGriffin(griffin):
    enemy = griffin.findNearestEnemy()
    if enemy:
        hero.command(griffin, "attack", enemy)


def commandPeasant(peasant):
    item = peasant.findNearestItem()
    if item:
        hero.command(peasant, "move", item.pos)


def summonGriffins():
    if hero.gold >= hero.costOf("griffin-rider"):
        hero.summon("griffin-rider")


while True:
    commandFriends()
    summonGriffins()
