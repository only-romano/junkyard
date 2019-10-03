def chooseStrategy():
    enemies = hero.findEnemies()
    if hero.gold >= hero.costOf("griffin-rider"):
        return "griffin-rider"
    for enemy in enemies:
        if enemy.type == "fangrider" and enemy.pos.x < 55:
            return "fight-back"
    return "collect-coins"


def commandAttack():
    friends = hero.findFriends()
    for friend in friends:
        enemy = friend.findNearestEnemy()
        if enemy:
            hero.command(friend, "attack", enemy)


def pickUpCoin():
    item = hero.findNearestItem()
    if (item)
        hero.move(item.pos)


def heroAttack():
    enemy = hero.findNearestEnemy()
    if enemy:
        if hero.canCast("regen"):
            hero.cast("regen", hero)
        while enemy.health > 0:
            hero.attack(enemy)


while True:
    if hero.time > 55:
        if hero.isReady("reset-cooldown"):
            hero.resetCooldown("invisibility")
        if hero.canCast("invisibility"):
            hero.cast("invisibility", hero)
            hero.moveXY(100, 20)
        continue
    if hero.time > 50:
        if hero.canCast("invisibility"):
            hero.cast("invisibility", hero)
            hero.moveXY(100, 20)
    commandAttack()
    strategy = chooseStrategy()
    if strategy == "griffin-rider":
        hero.summon("griffin-rider")
    elif strategy == "fight-back":
        heroAttack()
    else:
        pickUpCoin()
