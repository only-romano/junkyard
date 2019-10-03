def dealEnemy(enemy):
    if enemy.type == "munchkin":
        hero.attack(enemy)
    if enemy.type == "brawler":
        hero.say("Bye Bye!")

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        dealEnemy(enemy)
    else:
        hero.moveXY(30, 34)
