lowestPossible = 1
highestPossible = 999
num = 0

while True:
    enemy = hero.findNearest(hero.findEnemies())
    if enemy:
        if enemy.type == "scout":
            lowestPossible = num
        elif enemy.type == "munchkin":
            highestPossible = num
        hero.attack(enemy)
    else:
        num = lowestPossible + Math.ceil((highestPossible - lowestPossible) / 2);
        hero.say(num)
