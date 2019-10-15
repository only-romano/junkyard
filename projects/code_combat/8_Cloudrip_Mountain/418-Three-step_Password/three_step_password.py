hero.moveXY(52, 50)
message = hero.findNearest(hero.findFriends()).message

hero.moveXY(66, 34)
separator = hero.findNearest(hero.findFriends()).separator

hero.moveXY(52, 18)
index = hero.findNearest(hero.findFriends()).index

hero.moveXY(44, 34)
hero.say(message.split(separator)[index])


while True:
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 45:
        hero.attack(enemy)
