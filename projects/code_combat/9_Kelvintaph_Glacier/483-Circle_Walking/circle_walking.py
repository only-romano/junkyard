center = new Vector(40, 34)
partner = hero.findByType("peasant")[0]

while True:
    vector = Vector.subtract(center, partner.pos)
    moveToPos = Vector.add(center, vector)
    hero.move(moveToPos)
