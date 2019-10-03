ordersGiven = 0

while ordersGiven < 5:
    hero.moveXY(hero.pos.x, hero.pos.y - 10)
    hero.say("Attack!")
    ordersGiven += 1

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
