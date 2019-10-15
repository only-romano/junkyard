def cleaveWhenClose(target):
    if hero.distanceTo(target) < 5:
        if hero.isReady("cleave"):
            hero.cleave(target)
        else:
            hero.attack(target)

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        cleaveWhenClose(enemy)
