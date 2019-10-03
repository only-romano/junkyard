def moveRight():
    hero.moveXY(hero.pos.x + 12, hero.pos.y)

def moveDown():
    hero.moveXY(hero.pos.x, hero.pos.y - 12)

def moveUp():
    hero.moveXY(hero.pos.x, hero.pos.y + 12)


moveRight()
moveDown()
moveUp()
moveUp()
moveRight()
