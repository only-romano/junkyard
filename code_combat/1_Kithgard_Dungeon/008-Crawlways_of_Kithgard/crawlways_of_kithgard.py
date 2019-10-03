"""
You need "Elemental codex 1+"" to cast "haste".
You need "Mimik" as companion.

original by lukasgr
"""
def getGem():
    pet.moveXY(27, 30)
    pet.moveXY(20, 30)

pet.on("spawn", getGem)
hero.cast("haste", hero)
hero.moveRight(1)
