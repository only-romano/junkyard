# Escape from the maze!
# Some doors are blocked, some open when you are near them.

distanceBetweenRooms = 16
startRoom = {"x": 18, "y": 19}

distance = 16
move = Vector(distance, 0)
direction = Vector.add(move, hero.pos)
while True:
    while not (hero.isPathClear(hero.pos, direction)):
        move = Vector.rotate(move, Math.PI / 2)
        direction = Vector.add(move, hero.pos)
        # hero.say(direction)
    hero.moveXY(direction.x, direction.y)
    move = Vector.rotate(move, -Math.PI / 2)
    direction = Vector.add(move, hero.pos)
