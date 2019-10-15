def getItems():
    item = hero.findNearestItem()
    if item:
        hero.moveXY(item.pos.x, item.pos.y)

def manualAttack():
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

while True:
    time = hero.time
    if time < 10 or hero.time > 35:
        manualAttack()
    else:
        getItems()
