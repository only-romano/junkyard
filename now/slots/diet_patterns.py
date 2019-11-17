try:
    from my_values import IDEAL_WEIGHT
except ImportError:
    # put your ideal weight here
    IDEAL_WEIGHT = 66.6

def DIET(slots):
    """
    weight = next(w for w in reversed(slots.weights) if w is not None)
    coef = weight / IDEAL_WEIGHT
    if coef > 1.5:
        return DP.STAGE_FAT(slots)
    elif coef > 1.25:
        return DP.STAGE_FATTY(slots)
    elif coef > 1.1:
        return DP.STAGE_OVERWEIGHT(slots)
    elif coef > 1.04:
        return DP.STAGE_TUMMY(slots)
    elif coef > 1.01:
        return DP.STAGE_OVERIDEAL(slots)
    elif coef > 0.99:
        return DP.STAGE_IDEAL(slots)
    elif coef > 0.96:
        return DP.STAGE_UNDERIDEAL(slots)
    elif coef > 0.9:
        return DP.STAGE_SLIM(slots)
    elif coef > 0.8:
        return DP.STAGE_THIN(slots)
    elif coef > 0.7:
        return DP.STAGE_SKINNY(slots)
    else:
        return DP.STAGE_ANOREXY(slots)
    """
    return "ДИЕТА"
