def growSquare(cx, cy, side):
    side = side / 2
    hero.moveXY(cx - side, cy + side)
    hero.toggleFlowers(True)
    hero.moveXY(cx - side, cy - side)
    hero.moveXY(cx + side, cy - side)
    hero.moveXY(cx + side, cy + side)
    hero.moveXY(cx - side, cy + side)
    hero.toggleFlowers(False)


keeper = hero.findNearest(hero.findFriends())
points = keeper.pointsForWork
squareSize = 8
hero.toggleFlowers(False)

for point in points:
    growSquare(point.x, point.y, squareSize)
