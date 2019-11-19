from datetime import date
from math import ceil
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

    diff = (weight_now / MVP['weight'] * 100 - 100)
    sign = -1 if diff < 0 else 1
    if diff <= -30 or diff >= 50:
        stage_number = sign * 5
    elif diff <= -20 or diff >= 25:
        stage_number = sign * 4
    elif abs(diff) >= 4:
        stage_number = sign * (3 if abs(diff) >= 10 else 2)
    else:
        stage_number = sign * 1 if abs(diff) >= 1 else 0

    values = {
        "weight_now": weight_now,
        "weight_ideal": MVP['weight'],
        "weight_diff": diff,
        "muscle_now": muscle_now,
        "fat_now": fat_now,
        "water_now": water_now,
        "diet_day": slots.diet_day,
        }
    return _diet_text(_stage_constructor(stage_number, values))


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
    "СТАДИЯ № %i\n" % abs(stage['number']),
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


def _stage_constructor(stage_number, values):
    nutrients = _get_nutrients(stage_number, values)
    return {
        "number": stage_number,
        "sport": _get_sport_rate_description(abs(stage_number)),
        "description": _get_stage_description(stage_number),
        "weight_min": _get_stage_min_weight(stage_number, values['weight_ideal']),
        "weight_max": _get_stage_max_weight(stage_number, values['weight_ideal']),
        "date_min": _get_stage_min_date(stage_number, values['weight_diff'], values['weight_ideal']),
        "date_med": _get_stage_med_date(stage_number, values['weight_diff'], values['weight_ideal']),
        "date_max": _get_stage_max_date(stage_number, values['weight_diff'], values['weight_ideal']),
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


def _get_sport_rate_description(stage_number):
    if stage_number > 3:
        rate = "МАЛАЯ" if stage_number == 5 else "СРЕДНЯЯ"
    elif stage_number > 1:
        rate = "ПОВЫШЕННАЯ" if stage_number == 3 else  "ВЫСОКАЯ"
    else:
        rate = "МАКСИМАЛЬНАЯ" if stage_number == 1 else "ПОДДЕРЖИВАЮЩАЯ"
    return "%s ИНТЕНСИВНОСТЬ НАГРУЗОК" % rate


def _get_stage_description(stage_number):
    if stage_number == 0:
        return "ПРАВИЛЬНОЕ ПИТАНИЕ И ПОДДЕРЖИВАЮЩИЕ НАГРУЗКИ ДЛЯ ОПТИМАЛЬНОЙ РАБОТЫ ОРГАНИЗМА"
    elif stage_number == -1:
        return "КОРРЕКЦИЯ ВЕСА С ПОМОЩЬЮ ПОВЫШЕННИЯ РАЦИОНА И МАКСИМАЛЬНЫХ НАГРУЗОК С НАБОРОМ МЫШЕЧНОЙ МАССЫ"
    elif stage_number == 1:
        return "КОРРЕКЦИЯ ВЕСА С ПОМОЩЬЮ ПРАВИЛЬНОГО ПИТАНИЯ И МАКСИМАЛЬНЫХ НАГРУЗОК С НАБОРОМ МЫШЕЧНОЙ МАССЫ"
    elif stage_number == -2:
        return "КОРРЕКЦИЯ ВЕСА С ПОМОЩЬЮ УВЕЛИЧЕННОГО РАЦИОНА И ВЫСОКИХ НАГРУЗОК С НАБОРОМ МЫШЕЧНОЙ МАССЫ"
    elif stage_number == 2:
        return "КОРРЕКЦИЯ ВЕСА С ПОМОЩЬЮ ОГРАНИЧЕННОГО ПИТАНИЯ И ВЫСОКИХ НАГРУЗОК С МИНИМАЛЬНЫМ НАБОРОМ МЫШЕЧНОЙ МАССЫ"
    elif stage_number == -3:
        return "НАБОР ВЕСА С ПОМОЩЬЮ ОБИЛЬНОГО РАЦИОНА И УСИЛЕННЫХ НАГРУЗОК С НАБОРОМ МЫШЕЧНОЙ МАССЫ"
    elif stage_number == 3:
        return "СБРОС ВЕСА С ПОМОЩЬЮ ТОЛЕРАНТНОЙ ДИЕТЫ И УСИЛЕННЫХ НАГРУЗОК БЕЗ ПОТЕРЬ МЫШЕЧНОЙ МАССЫ"
    elif stage_number == -4:
        return "НАБОР ВЕСА С ПОМОЩЬЮ ОБИЛЬНОГО РАЦИОНА И СРЕДНИХ НАГРУЗОК С МИНИМАЛЬНЫМ НАБОРОМ МЫШЕЧНОЙ МАССЫ"
    elif stage_number == 4:
        return "СБРОС ВЕСА С ПОМОЩЬЮ ДИЕТЫ И СРЕДНИХ НАГРУЗОК С МИНИМАЛЬНЫМИ ПОТЕРЯМИ МЫШЕЧНОЙ МАССЫ"
    elif stage_number == -5:
        return "НАБОР ВЕСА С ПОМОЩЬЮ ОБИЛЬНОГО РАЦИОНА И МИНИМАЛЬНЫХ НАГРУЗОК БЕЗ НАБОРА МЫШЕЧНОЙ МАССЫ"
    elif stage_number == 5:
        return "СБРОС ВЕСА С ПОМОЩЬЮ ЖЁСТКОЙ ДИЕТЫ И МИНИМАЛЬНЫХ НАГРУЗОК С ПОТЕРЕЙ МЫШЕЧНОЙ МАССЫ"


def _get_stage_min_weight(stage_number, ideal_weight):
    if stage_number == 0: coef = 0.99
    elif stage_number == 1: coef = 1.01
    elif stage_number == 2: coef = 1.04
    elif stage_number == 3: coef = 1.10
    elif stage_number == 4: coef = 1.25
    elif stage_number == 5: coef = 1.50
    elif stage_number == -1: coef = 0.96
    elif stage_number == -2: coef = 0.90
    elif stage_number == -3: coef = 0.80
    elif stage_number == -4: coef = 0.70
    elif stage_number == -5: coef = 0.50
    # return
    return ideal_weight * coef


def _get_stage_max_weight(stage_number, ideal_weight):
    if stage_number == 0: coef = 1.01
    elif stage_number == 1: coef = 1.04
    elif stage_number == 2: coef = 1.10
    elif stage_number == 3: coef = 1.25
    elif stage_number == 4: coef = 1.50
    elif stage_number == 5: coef = 2.00
    elif stage_number == -1: coef = 0.99
    elif stage_number == -2: coef = 0.96
    elif stage_number == -3: coef = 0.90
    elif stage_number == -4: coef = 0.80
    elif stage_number == -5: coef = 0.70
    # return
    return ideal_weight * coef - 0.1


def _get_stage_min_date(stage_number, weight_diff, ideal_weight):
    if stage_number == 0: return ""
    elif abs(stage_number) == 1: stage_coef = 1
    elif abs(stage_number) == 2: stage_coef = 4
    elif abs(stage_number) == 3: stage_coef = 10
    elif stage_number == 4: stage_coef = 25
    elif stage_number == 5: stage_coef = 50
    elif stage_number == -4: stage_coef = 20
    elif stage_number == -5: stage_coef = 30
    else: return ""
    # return
    coef = ceil((weight_diff-stage_coef) * (ideal_weight/abs(stage_number))**0.5)
    return date.fromordinal(date.today().toordinal()+coef).strftime("%d %b %Y")


def _get_stage_med_date(stage_number, weight_diff, ideal_weight):
    if stage_number == 0: return "ИДЕАЛ"
    return _get_stage_min_date(stage_number, weight_diff, ideal_weight*2)


def _get_stage_max_date(stage_number, weight_diff, ideal_weight):
    return _get_stage_min_date(stage_number, weight_diff, ideal_weight*4)


def _get_nutrients(stage_number, values):
    swing = _get_swing(values['diet_day'])
    muscle_diff = (values['muscle_now'] / MVP['muscle'] * 100 - 100)
    fat_diff = (values['fat_now'] / MVP['fat'] * 100 - 100)
    water_diff = (values['water_now'] / MVP['water'] * 100 - 100)
    
"""
    values = {
        "weight_now": weight_now,
        "weight_ideal": MVP['weight'],
        "weight_diff": diff,
        "muscle_now": muscle_now,
        "muscle_ideal": MVP['muscle'],
        "fat_now": fat_now,
        "fat_ideal": MVP['fat'],
        "water_now": water_now,
        "water_ideal": MVP['water'],
        "diet_day": slots.diet_day,
        }
"""

def _get_swing(diet_day):
    celebration_swing = {
        "name": "Праздничные Качели",
        "calories": 1.5,
        "protein": 1.0,
        "carbonate": 1.5,
        "fat": 2.0,
        }

    complex_swing = {
        "name": "Комплексные Качели",
        "calories": 1.3,
        "protein": 1.15,
        "carbonate": 1.25,
        "fat": 1.5,
    }

    sugar_swing = {
        "name": "Углеводные Качели",
        "calories": 1.15,
        "protein": 1.0,
        "carbonate": 1.25,
        "fat": 1.2,
    }

    balance_swing = {
        "name": "Балансовые Качели",
        "calories": 0.8,
        "protein": 0.9,
        "carbonate": 0.7,
        "fat": 0.5,
    }

    try:
        from my_values import celebrations #, holidays, special_days, tuff_days
    except ImportError:
        celebrations = None

    if celebrations:
        today = date.today().toordinal()
        if today in celebrations:
            celebration_swing.update({"name": celebrations[today]})
            return celebration_swing
    else diet_day == 17:
        return celebration_swing

    if diet_day in [5, 23]:
        return complex_swing
    if diet_day in [11, 29]:
        return sugar_swing
    if diet_day in [2, 6, 8, 12, 14, 18, 20, 24, 26, 30]:
        return balance_swing
    

