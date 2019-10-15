partner = hero.findNearest(hero.findFriends())
yDif = hero.pos.y - partner.pos.y
xDif = hero.pos.x - partner.pos.x

while True:
    hero.move({"x": partner.pos.x + xDif, "y": partner.pos.y + yDif})
