while True:
    gem = hero.findNearest(hero.findItems())
    if gem:
        if hero.isPathClear(hero.pos, gem.pos):
            hero.move(gem.pos)
        else:
            hero.move({"x": 40, "y": 35})
        
        