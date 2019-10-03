def dynamicMaxSum (gems):
    cycles = 0
    maxStartIndex = 0
    maxEndIndex = 0
    maxEndHere = 0
    currentStartIndex = 0
    maxBest = 0
    for i in range(len(gems)):
        cycles += 1
        maxEndHere += gems[i].value
        if maxEndHere < 0:
            maxEndHere = 0
            currentStartIndex = i + 1
        if maxEndHere > maxBest:
            maxStartIndex = currentStartIndex
            maxEndIndex = i
            maxBest = maxEndHere
    hero.say("I's taken " + cycles + " cycles.")
    return [maxStartIndex, maxEndIndex]


def naiveMaxSum(gems):
    cycles = 0
    maxStartIndex = 0
    maxEndIndex = 0
    maxBest = 0
    for i in range(len(gems)):
        sums = 0
        for j in range(i, len(gems)):
            cycles += 1
            if cycles > 104:
                hero.say("I fed up of calculations.")
                return [i, j]
            sums += gems[j].value
            if sums > maxBest:
                maxStartIndex = i
                maxEndIndex = j
                maxBest = sums
    hero.say("I's taken " + cycles + " cycles.")
    return [maxStartIndex, maxEndIndex]


items = hero.findItems()
edges = naiveMaxSum(items)

x1 = edges[0] * 4 + 4
x2 = edges[1] * 4 + 4

hero.moveXY(x1, 40)
hero.moveXY(x2, 40)
hero.moveXY(40,64)
