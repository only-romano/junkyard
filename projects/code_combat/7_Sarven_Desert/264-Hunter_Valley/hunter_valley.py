def moveDownRight(shift):
    hero.moveXY(hero.pos.x + shift, hero.pos.y - shift)


def moveUpRight(shift):
    hero.moveXY(hero.pos.x + shift, hero.pos.y + shift)


hunter = hero.findFriends()[0]
route = hunter.route
routeIndex = 0

while routeIndex < route.length:
    direction = route[routeIndex]
    routeIndex += 1;
    if direction > 0:
        moveUpRight(8)
    else:
        moveDownRight(8)
