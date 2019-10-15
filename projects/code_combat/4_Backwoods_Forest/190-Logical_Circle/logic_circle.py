def logic(value, a, b):
    if value:
        return a
    return b

hero.moveXY(20, 24);
a = hero.findNearestFriend().getSecretA()
b = hero.findNearestFriend().getSecretB()
c = hero.findNearestFriend().getSecretC()

hero.moveXY(30, logic(a and b and c, 33, 15))
hero.moveXY(logic(a or b or c, 20, 40), 24)
hero.moveXY(30, logic(a and b and c, 33, 15))
