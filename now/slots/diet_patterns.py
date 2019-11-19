try:
    from my_values import my_values_preset as MVP
except ImportError:
    # put your values here
    height =  None              # your height in sm (inches * 2.54)
    age = None                  # your age
    gender = None               # to correct formula gender needed (available options: "M" for male, "F" for female, "T" for transgender)
    muscle = None               # a lot of muscles?
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
    return _diet_text(_stage_constructor())


def get_MVP(height, age, gender, muscle, d_weight=None):
    return {
        "weight": 66.6,
        "muscle": 27.5,
        "fat": 15.0,
        "water": 50.0,
        "IMT": (d_weight / height**2 if d_weight and height else 22.5),
        }


# internal use functions
def _diet_text(stage):
    return "\t\tДиета на сегодня. " + "\n\t\t\t".join([
    "СТАДИЯ № %i\n" % stage['number'],
    stage['sport'],
    stage['description'] + "\n",
    "ПОКАЗАТЕЛИ:     %.1f - %.1f кГ" % (stage['weight_min'], stage['weight_max']),
    "РАСЧЁТН. ВРЕМЯ: %s ... (%s) ... %s" % (stage['date_min'], stage['date_med'], stage['date_max']),
    "%s" % ("\n\t\t\t" + stage['swing'] + "\n" if stage['swing'] else ""),
    _get_element_value("БЕЛОК:", stage['protein']),
    _get_element_value("САХАР:", stage['carbonate']),
    _get_element_value("ЖИРЫ: ", stage['fat']) + "\n",
    "ККАЛ:     %i - %i ККал" % (stage['calories']['min'], stage['calories']['max'])
    ])


def _stage_constructor():
    return {
        "number": 0,
        "sport": "sport",
        "description": "description",
        "weight_min": 0.0,
        "weight_max": 0.0,
        "date_min": "01 jan 1970",
        "date_med": "19 jan 2020",
        "date_max": "20 mar 2020",
        "swing": "",
        "calories": {
            "min": 0,
            "max": 0,
            },
        "protein": {
            "mass": {
                "min": 0,
                "max": 0,
                },
            "per_kg": {
                "min": 0,
                "max": 0,
                },
            "procent": 0.0,
            },
        "carbonate": {
            "mass": {
                "min": 0,
                "max": 0,
                },
            "per_kg": {
                "min": 0,
                "max": 0,
                },
            "procent": 0.0,
            },
        "fat": {
            "mass": {
                "min": 0,
                "max": 0,
                },
            "per_kg": {
                "min": 0,
                "max": 0,
                },
            "procent": 0.0,
            },
        }


def _get_element_value(label, values):
    return "%s    %i - %i гр   (~ %i - %i мг/кГ)  -  [%.1f %%]" % (
            label,
            values['mass']['min'],
            values['mass']['max'],
            values['per_kg']['min'],
            values['per_kg']['max'],
            values['procent']
        )
