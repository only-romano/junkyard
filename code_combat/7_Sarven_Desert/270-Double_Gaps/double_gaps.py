def moveDownCenter():
    hero.moveXY(40, hero.pos.y - 12)

def buildRightOf(something):
    hero.buildXY("fence", something.pos.x + 20, something.pos.y)

def buildLeftOf(something):
    hero.buildXY("fence", something.pos.x - 20, something.pos.y)

while True:
    ogre = hero.findNearestEnemy()
    coin = hero.findNearestItem()
    if ogre:
        buildLeftOf(ogre)
    if coin:
        buildRightOf(coin)
    moveDownCenter()
