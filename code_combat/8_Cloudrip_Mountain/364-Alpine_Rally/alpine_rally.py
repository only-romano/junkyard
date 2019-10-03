hero.cast("haste", hero);

while True:
    if hero.pos.x > 100:
        hero.manaBlast()
    if hero.pos.x > 150:
        hero.resetCooldown("haste")
    if hero.canCast("haste"):
        hero.cast("haste", hero)
    hero.move({"x": 273, "y": 35})
