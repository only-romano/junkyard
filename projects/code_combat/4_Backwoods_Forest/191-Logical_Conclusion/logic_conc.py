def goTo(logic, x, y):
    hero.moveXY(x, y)
    hero.say(logic)

hero.moveXY(26, 16);
a = hero.findNearestFriend().getSecretA()
b = hero.findNearestFriend().getSecretB()
c = hero.findNearestFriend().getSecretC()

goTo(a and b or c, 25, 26)
goTo((a or b) and c, 26, 32)
goTo((a or c) and (b or c), 35, 32)
goTo((a and b) or (not c and b), 40, 22)
