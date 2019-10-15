def goTo(pos):
    while hero.pos.x < pos.x - 5:
        hero.move({"x": pos.x - 5, "y": 35})
    while hero.pos.x < pos.x:
        hero.move(pos)


gems = hero.findItems();

for gem in gems:
    goTo(gem.pos)
