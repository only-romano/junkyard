def almostEqual(valueA, valueB):
    return valueA > 0.97 * valueB and valueA < 1.03 * valueB


def perimeter(side1, side2):
    return (side1 + side2) * 2


def area(side1, side2):
    return side1 * side2


requiredPerimeter = 104
requiredArea = 660
base = hero.findNearest(hero.findFriends())

while True:
    sideSN = base.distanceTo("Femae")
    sideWE = base.distanceTo("Illumina")
    currentPerimeter = perimeter(sideSN, sideWE)
    currentArea = area(sideSN, sideWE)
    if almostEqual(currentArea, requiredArea) and almostEqual(currentPerimeter, requiredPerimeter):
        hero.say("VENITE!")
        break
