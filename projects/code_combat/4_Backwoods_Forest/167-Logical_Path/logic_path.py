def goFurther(logic, x):
    if logic:
        hero.moveXY(x, 33)
    else:
        hero.moveXY(x, 15)
    hero.moveXY(x + 6, 24)

hero.moveXY(14, 24)
a = hero.findNearestFriend().getSecretA()
b = hero.findNearestFriend().getSecretB()

arr = [a and b, a or b, not b]
x = 20

for i in arr:
    goFurther(i, x)
    x += 12
