innerRadius = hero.distanceTo(hero.findNearestItem())


def definitelyGreater(a, b):
    return a > b + 0.5

center = {"x": 40, "y": 34}
gems = hero.findItems()

for gem in gems:
    if definitelyGreater(hero.distanceTo(gem), innerRadius);
        hero.moveXY(gem.pos.x, gem.pos.y)
        hero.moveXY(center["x"], center["y"])
