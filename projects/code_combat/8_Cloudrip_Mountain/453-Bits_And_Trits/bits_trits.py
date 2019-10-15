def to_sys(numberm, num):
    string = ""
    while number != 0:
        remainder = number % num
        number = (number - remainder) / num
        string = remainder + string
    return string


def findMostDangerous(enemies):
    mostDangerous = None
    mostHealth = -99999
    for enemy in enemies:
        if enemy.health > mostHealth:
            mostDangerous = enemy
            mostHealth = enemy.health
    return mostDangerous


while True:
    dangerous = findMostDangerous(hero.findEnemies())
    if dangerous:
        hero.say(to_sys(dangerous.health, 3) + " " + to_sys(dangerous.type, 2))
