# To cast "Haste" you need an Elemental codex 1+

hero.cast("haste", hero)
hero.moveXY(55, 14)
hero.moveXY(92, 9)

hero.buildXY("fire-trap", 94, 19)
hero.moveXY(55, 14)
hero.cast("haste", hero)
hero.buildXY("fire-trap", 90, 52)
hero.buildXY("fire-trap", 61, 61)
hero.say("retreat")
hero.moveXY(-12, 34)
