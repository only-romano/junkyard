def pickUpCoin():
    item = hero.findNearestItem()
    if item:
        hero.move(item.pos)


def summonTroops():
    if hero.gold >= hero.costOf("soldier"):
        hero.summon("soldier")


def commandSoldier(soldier):
    enemy = soldier.findNearestEnemy()
    if enemy:
        hero.command(soldier, "attack", enemy)


def commandArcher(archer):
    enemy = archer.findNearestEnemy()
    if enemy and archer.distanceTo(enemy) <= 25:
        hero.command(archer, "attack", enemy)
    else:
        hero.command(archer, "move", archer.pos)


while True:
    pickUpCoin()
    summonTroops()
    friends = hero.findFriends()
    for friend in friends:
        if friend.type == "soldier":
            hero.commandSoldier(friend)
        else friend.type == "archer":
            hero.commandArcher(friend)
