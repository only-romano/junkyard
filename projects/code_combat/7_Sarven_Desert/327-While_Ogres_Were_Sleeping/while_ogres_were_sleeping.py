points = [
    {x: 21, y: 8}, {x: 33, y: 8}, {x: 45, y: 8},
    {x: 57, y: 8}, {x: 68, y: 8}, {x: 68, y: 18},
    {x: 68, y: 28}, {x: 68, y: 38}, {x: 68, y: 48},
    {x: 68, y: 58}, {x: 56, y: 58}, {x: 44, y: 58}, 
    {x: 32, y: 58}, {x: 20, y: 58}, {x: 10, y: 60}
]

pointIndex = 0;

while pointIndex < len(points):
    point = points[pointIndex]
    hero.moveXY(point.x, point.y)
    enemy = hero.findNearestEnemy()
    coin = hero.findNearestItem()
    if enemy.team == "ogres" and enemy.health < 10:
        hero.attack(enemy)
    if coin.value < 5 and hero.distanceTo(coin) < 7:
        hero.moveXY(coin.pos.x, coin.pos.y)
    if enemy.type == "skeleton" and enemy.health < 10:
        hero.attack(enemy)
    pointIndex += 1
