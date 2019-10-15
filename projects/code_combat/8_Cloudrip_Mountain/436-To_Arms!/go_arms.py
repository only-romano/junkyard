sergeant =  hero.findNearest(hero.findFriends())
stepX = sergeant.tentDistanceX
stepY = sergeant.tentDistanceY
tentsInRow = 5
tentsInColumn = 4
firstX = 10
firstY = 14
finalX = firstX + tentsInRow * stepX
finalY = firstY + tentsInColumn * stepY

for y in range(firstY, finalY, stepY):
    for x in range(firstX, finalX, stepX):
        hero.moveXY(x, y)
        hero.say("War!")

while True:
    friend = hero.findNearest(hero.findFriends())
    if friend and hero.canCast("grow"):
        hero.cast("grow", friend)
    if friend and hero.canCast("regen"):
        hero.cast("regen", friend)
