def summonAndSend(type, x, y):
    hero.summon(type)
    var unit = hero.built[-1]
    hero.command(unit, "move", {"x": x, "y": y})


centerUnit = hero.findNearest(hero.findFriends())
center = centerUnit.pos
rectWidth = centerUnit.rectWidth
rectHeight = centerUnit.rectHeight

leftBottomX = center.x - rectWidth / 2
leftBottomY = center.y - rectHeight / 2
summonAndSend("soldier", leftBottomX, leftBottomY)

leftTopX = center.x - rectWidth / 2
leftTopY = center.y + rectHeight / 2
summonAndSend("archer", leftTopX, leftTopY)

rightTopX = center.x + rectWidth / 2
rightTopY = center.y + rectHeight / 2
summonAndSend("soldier", rightTopX, rightTopY)

rightBottomX = center.x + rectWidth / 2
rightBottomY = center.y - rectHeight / 2
summonAndSend("archer", rightBottomX, rightBottomY)

while True:
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 10:
        hero.attack(enemy)
