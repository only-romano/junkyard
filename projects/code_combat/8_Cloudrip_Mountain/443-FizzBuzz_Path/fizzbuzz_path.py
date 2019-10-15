steps = 1

while True:
    if steps % 3 == 0 and steps % 5 == 0:
        hero.moveXY(hero.pos.x - 10, hero.pos.y + 10)
    elif steps % 3 == 0:
        hero.moveXY(hero.pos.x + 10, hero.pos.y)
    elif steps % 5 == 0:
        hero.moveXY(hero.pos.x - 10, hero.pos.y)
    else:
        hero.moveXY(hero.pos.x, hero.pos.y + 10)
    steps += 1
