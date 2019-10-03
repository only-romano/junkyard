while True:
    angle = Math.PI / 2 - Math.PI / 16
    while angle >= -Math.PI / 2:
        targetX = hero.pos.x + 5 * Math.cos(angle)
        targetY = hero.pos.y + 5 * Math.sin(angle)
        target = {"x": targetX, "y": targetY}
        if hero.isPathClear(hero.pos, target):
            hero.move(target)
        else:
            angle -= Math.PI / 16
