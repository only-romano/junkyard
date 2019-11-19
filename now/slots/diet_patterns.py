try:
    from my_values import my_values_preset as MVP
except ImportError:
    from diet_patterns import get_MVP
    # put your values here
    height =  180               # your height in sm (inches * 2.54)
    age = 25                    # your age
    gender = "M"                # i'm sorry but to correct formula gender needed (available options: "M" for male, "F" for female, "T" for transgender)
    muscle = False              # a lot of muscles?
    desirable_weight = None     # leave None to auto-calculate else input float
    MVP = get_MVP(height, age, gender, muscle, desirable_weight)


def DIET(slots):
    weight_now = next((w for w in reversed(slots.weight) if w is not None), None)
    muscle_now = next((m for m in reversed(slots.muscle) if m is not None), None)
    fat_now = next((f for f in reversed(slots.fat) if f is not None), None)
    water_now = next((w for w in reversed(slots.water) if w is not None), None)
    """
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


def get_MVP(height, age, gender, muscle, desirable_weight=None):
    return {
        "weight": None,
        "muscle": None,
        "fat": None,
        "water": None,
        "IMT": None,
        }
