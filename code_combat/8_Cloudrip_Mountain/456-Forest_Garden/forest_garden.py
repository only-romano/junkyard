gardener = hero.findNearest(hero.findFriends())
gardenWidth = gardener.gardenWidth
gardenHeight = gardener.gardenHeight

hero.toggleFlowers(True)
x = hero.pos.x
y = hero.pos.y

hero.moveXY(x, y - gardenHeight)
hero.moveXY(x + gardenWidth, y - gardenHeight)
hero.moveXY(x + gardenWidth, y)
hero.moveXY(x, y)
