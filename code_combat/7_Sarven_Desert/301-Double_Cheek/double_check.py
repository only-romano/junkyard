defeatedOgres = 0

while defeatedOgres < 6:
    enemy = hero.findNearestEnemy()
    if enemy:
        while enemy.health > 0:
            hero.attack(enemy)

        defeatedOgres += 1
    else:
        hero.say("Ogres!")

hero.moveXY(55, 36)

while hero.gold < 30:
    item = hero.findNearestItem()
    if item:
        hero.moveXY(item.pos.x,item.pos.y)

hero.moveXY(76, 32)
