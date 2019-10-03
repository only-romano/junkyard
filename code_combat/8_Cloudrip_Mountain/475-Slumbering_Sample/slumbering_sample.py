def avgSize(units):
    if units.length == 0
        return 0
    total = 0
    for unit in units:
        total += unit.size
    return total / units.length


hero.say(avgSize(hero.findByType("yeti")))
