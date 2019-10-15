def fightAndReport(untilTime):
    defeated = 0
    while True:
        enemy = hero.findNearestEnemy()
        if enemy:
            hero.attack(enemy)
            if enemy.health <= 0:
                defeated += 1
        if hero.time > untilTime:
            break;
    hero.moveXY(59, 33)
    hero.say(defeated)


fightAndReport(15)

while True:
    item = hero.findNearestItem()
    if item:
        hero.moveXY(item.pos.x, item.pos.y)
    if hero.time > 30:
        break

hero.say(hero.gold)
fightAndReport(45)
