potionCount = 0

while potionCount != 7:
    item = hero.findNearestItem()
    if item:
        hero.moveXY(item.pos.x, item.pos.y)
        potionCount += 1

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
