def checkToDefend(target="Door"):
    hero.attack(target)

while True:
    enemy = hero.findNearestEnemy()
    checkToDefend(enemy)
