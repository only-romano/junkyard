def maybeBuildTrap(x, y):
    hero.moveXY(x, y)
    item = hero.findNearestItem()
    if item and item.type == "coin":
        hero.buildXY("fire-trap", x, y)

while True:
    maybeBuildTrap(12, 56)
    maybeBuildTrap(68, 56)
    maybeBuildTrap(68, 12)
    maybeBuildTrap(12, 12)
