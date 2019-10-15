def areAntipodes(unit1, unit2):
    reversed1 = unit1.id.split("").reverse().join("")
    return reversed1 === unit2.id


friends = hero.findFriends()
enemies = hero.findEnemies()

for friend in friends:
    for enemy in enemies:
        if areAntipodes(friend, enemy):
            hero.command(friend, "move", enemy.pos)

hero.wait(5)
warlock = hero.findByType("warlock")[0]
while warlock.health > 0:
    hero.attack(warlock)
