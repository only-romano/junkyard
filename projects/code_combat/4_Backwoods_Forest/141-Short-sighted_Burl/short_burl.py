def takeItem(item):
    hero.moveXY(item.pos.x, item.pos.y)

def checkTakeRun(item):
    if item:
        takeItem(item)
    hero.moveXY(40, 13)


while True:
    hero.moveXY(16, 56)
    coin = hero.findNearestItem()
    checkTakeRun(coin)
    
    hero.moveXY(64, 56)
    coin = hero.findNearestItem()
    checkTakeRun(coin)
