perimeter = 160
area = 0
bottomLeft = {x: hero.pos.x, y: hero.pos.y}

topLeft = hero.findHazards()[0].pos
height = hero.distanceTo(topLeft)
width = perimeter / 2 - height

hero.buildXY("fire-trap", bottomLeft.x, bottomLeft.y)
hero.buildXY("fire-trap", bottomLeft.x + width, bottomLeft.y)
hero.buildXY("fire-trap", bottomLeft.x + width, bottomLeft.y + height)

hero.moveXY(74, 32)
area = height * width
hero.say(area)
