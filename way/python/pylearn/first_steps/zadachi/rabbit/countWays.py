def countWays(steps, maxJump):
    variants = []

    for step in range(steps, 1, -1):
        var1 = [1] * step
        if sum(var1) == steps:
            variants.append(var1)
            continue
        if maxJump > 1:

            for position in range(0, step):
                var2 = var1[:]
                for jump in range(2, maxJump + 1):
                    var2[position] = jump
                    if sum(var2) == steps and var2 not in variants:
                        variants.append(var2)
                        break

                    elif position + 1 != step:

                        for newPosition in range(position + 1, step):
                            var3 = var2[:]
                            for newJump in range(2, maxJump + 1):
                                var3[newPosition] = newJump
                                if sum(var3) == steps and var3 not in variants:
                                    variants.append(var3)
                                    break
                            else:
                                break
    return variants

print(countWays(4,3))

"""
def CountWays(steps, maxJump, variants=[]):
    if variants == []:
        variants.append(steps)
        variants.append([1]*steps)
    if maxJump > 1:
        variants = CountHelp(steps, maxJump, variants)
    return variants[1:]

def CountHelp(steps, maxJump, variants):
    for jumpIndex in range(0, steps):
        tempVariant = [1]*steps
        for jump in range(2, maxJump+1):
            tempVariant[jumpIndex] = jump
            if sum(tempVariant) == variants[0] and tempVariant not in variants:
                variants.append(tempVariant)
    return variants


print(CountWays(3,2))
"""