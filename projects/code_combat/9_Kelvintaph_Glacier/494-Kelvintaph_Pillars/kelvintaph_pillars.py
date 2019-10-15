def findMax(stack):
    maxSize = 0
    maxim = None
    for peasant in stack:
        if peasant.size > maxSize:
            maxSize = peasant.size
            maxim = peasant
    return maxim


def notEmpty(stack):
    return not (len(stack.viewStack()) == 0)


def movePeasant(out, to):
    hero.pickUpItem(out)
    hero.dropItem(to)


def moveNextItem(s1, s2, s3):
    if s1.peekItem() == findMax(s1.viewStack() + s2.viewStack()):
        movePeasant(s1, s3)
    else:
        movePeasant(s1, s2)


stump1 = hero.findByType('stump')[0]
stump2 = hero.findByType('stump')[1]
stump3 = hero.findByType('stump')[2]

while notEmpty(stump1) or notEmpty(stump2):
    while notEmpty(stump1):
        moveNextItem(stump1, stump2, stump3)
    while notEmpty(stump1):
        moveNextItem(stump2, stump1, stump3)
