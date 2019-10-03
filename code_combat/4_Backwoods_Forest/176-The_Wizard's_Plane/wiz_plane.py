def goTo(x, y, message):
    hero.moveXY(x, y)
    hero.say(message)
    return message

def getFirst(x):
    return x * 3 - 2

def getSecond(x):
    return (getFirst(x) - 1) * 4

def getThird(x):
    return (getFirst(x) + getSecond(x)) / 2

def getFourth(x):
    return (getFirst(x) + getSecond(x)) * (getSecond(x) - getThird(x))

hero.cast("haste", hero)
hero.moveXY(16, 32)
a = hero.findNearestFriend().getSecret()
logic = [getFirst, getSecond, getThird, getFourth]

for i in range(4):
    goTo(24 + i * 8, 28 - i * 4, logic[i](a))
