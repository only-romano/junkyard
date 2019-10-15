# To cast "Haste" you need an Elemental codex 1+
# You need the Mimic companion to make him work

def onSpawn():
    pet.moveXY(55, 47)
    pet.moveXY(31, 47)

pet.on("spawn", onSpawn)

hero.cast("haste", hero)

hero.moveXY(33, 24)
hero.moveXY(32, 47)
hero.moveXY(50, 47)
