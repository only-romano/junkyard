from datetime import date
from math import ceil
try:
    from my_values import my_values_preset as MVP
    from my_values import celebrations, fetes, holidays, rituals
except ImportError:
    try:
        from my_values_placeholder import my_values_preset as MVP
        from my_values_placeholder import celebrations, fetes, holidays, rituals
    except ImportError:
        MVP = get_MVP()
        celebrations, fetes, holidays, rituals = None, None, None, None


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


def get_MVP():
    return {
        "weight": 66.6,
        "muscle": 27.5,
        "fat": 15.0,
        "water": 57.5,
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
    "ККАЛ:    %4i - %4i ККал" % (stage['calories']['min'], stage['calories']['max']),
    "ВОДА:    %4i - %4i мл" % (stage['water']['min'], stage['water']['max']),
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
        "swing": nutrients['swing'],
        "calories": nutrients['calories'],
        "water": nutrients['water'],
        "protein": nutrients['protein'],
        "carbonate": nutrients['carbonate'],
        "fat": nutrients['fat']
        }


def _get_element_value(label, values):
    return "%s    %3i - %3i гр   (~ %4i - %4i мг/кГ)  -  [%4.1f %%]" % (
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
    # return "%s ВЕСА С ПОМОЩЬЮ %s НАГРУЗОК %s МЫШЕЧНОЙ МАССЫ" % (weight, diet_sport, muscle)


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
    return ideal_weight * coef + (0 if stage_number > 0 else 0.1)


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
    return ideal_weight * coef - (0 if stage_number < 0 else 0.1)


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
    diff = abs(weight_diff)
    coef = ceil((diff-stage_coef)*(ideal_weight/abs(stage_number))**0.5)
    return date.fromordinal(date.today().toordinal()+coef).strftime("%d %b %Y")


def _get_stage_med_date(stage_number, weight_diff, ideal_weight):
    if stage_number == 0: return "ИДЕАЛ"
    return _get_stage_min_date(stage_number, weight_diff, ideal_weight*2)


def _get_stage_max_date(stage_number, weight_diff, ideal_weight):
    return _get_stage_min_date(stage_number, weight_diff, ideal_weight*4)


def _get_nutrients(stage_number, values):
    swing = _get_swing(values['diet_day'])
    proteins = _get_proteins(stage_number, values, swing)
    carbonates = _get_carbonates(stage_number, values, swing)
    fats = _get_fats(stage_number, values, swing)
    calories = _get_calories(proteins, carbonates, fats)
    proteins['procent'] = proteins['mass']['max'] * 420 / calories['max']
    carbonates['procent'] = carbonates['mass']['max'] * 420 / calories['max']
    fats['procent'] = fats['mass']['max'] * 930 / calories['max']

    return {
        "swing": swing['name'] if swing else "",
        "calories": calories,
        "water": _get_water_values(values),
        "protein": proteins,
        'carbonate': carbonates,
        "fat": fats,
        }


def _get_proteins(stage_number, values, swing):
    muscle_diff = (values['muscle_now'] / MVP['muscle'] * 100 - 100)
    min_coef = 1.75 - abs(values['weight_diff'])*0.015
    min_coef = min_coef if min_coef >= 0.4 else 0.4
    max_coef = 2.5 - abs(values['weight_diff'])*0.027
    max_coef = max_coef if max_coef >= 0.45 else 0.45
    p_min = values['weight_now'] * (min_coef - muscle_diff*0.01)
    p_max = values['weight_now'] * (max_coef - muscle_diff*0.02)
    if swing:
        p_min *= swing['protein']
        p_max *= swing['protein']
    return _get_element(p_min, p_max, values['weight_now'])


def _get_carbonates(stage_number, values, swing):
    diff = values['weight_diff'] if values['weight_diff'] > 0 else values['weight_diff']/4
    fat_mass = (values['fat_now'] - MVP['fat']) * values['weight_now'] / 100
    min_coef = 3.5 - diff*0.04
    max_coef = 4.5 - diff*0.05
    min_coef = min_coef if min_coef >= 0.75 else 0.75
    max_coef = max_coef if max_coef >= 1.25 else 1.25
    if stage_number < 1:
        max_coef += 1
    c_min = values['weight_now'] * (min_coef - fat_mass * 0.0075)
    c_max = values['weight_now'] * (max_coef - fat_mass * 0.015)
    if swing:
        c_min *= swing['carbonate']
        c_max *= swing['carbonate']
    return _get_element(c_min, c_max, values['weight_now'])


def _get_fats(stage_number, values, swing):
    fat_mass = (values['fat_now'] - MVP['fat']) * values['weight_now'] / 100
    if fat_mass > 50:
        fat_mass = 50
    diff = values['weight_diff'] if values['weight_diff'] > 0 else values['weight_diff']/4
    min_coef = 1.25 - diff*0.02
    min_coef = min_coef if min_coef >= 0.5 else 0.5
    max_coef = 1.75 - diff*0.035
    max_coef = max_coef if max_coef >= 0.75 else 0.75
    #if stage_number == 2:
    #    max_coef = max_coef if max_coef < 1.5 else 1.5
    #elif stage_number == 3:
    #    max_coef = max_coef if max_coef < 1.33 else 1.33
    #elif stage_number == 4:
    #    max_coef = max_coef if max_coef < 1.25 else 1.25
    #elif stage_number == 5:
    #    max_coef = max_coef if max_coef < 1 else 1
    f_min = values['weight_now'] * (min_coef - fat_mass * 0.0075)
    f_max = values['weight_now'] * (max_coef - fat_mass * 0.01)
    if swing:
        f_min *= swing['fat']
        f_max *= swing['fat']
    return _get_element(f_min, f_max, values['weight_now'])


def _get_water_values(values):
    water_diff = (values['water_now'] / MVP['water'] * 100 - 100)
    weight_diff = values['weight_diff'] or 1
    water_base = values['weight_ideal'] + (weight_diff/abs(weight_diff)**0.5)
    return {
        "min": water_base * (25 - water_diff/2),
        "max": water_base * (35 - water_diff),
        }


def _get_calories(p, c, f):
    min = (p['mass']['min'] + c['mass']['min']) * 4.2 + f['mass']['min'] * 9.3
    max = (p['mass']['max'] + c['mass']['max']) * 4.2 + f['mass']['max'] * 9.3
    return {
        "min": min,
        "max": max
        }


def _get_swing(diet_day):
    celebration_swing = {
        "name": "Праздничные Качели",
        # "calories": 1.5,
        "protein": 1.0,
        "carbonate": 1.5,
        "fat": 2.0,
        }
    complex_swing = {
        "name": "Комплексные Качели",
        # "calories": 1.3,
        "protein": 1.15,
        "carbonate": 1.25,
        "fat": 1.5,
    }
    sugar_swing = {
        "name": "Углеводные Качели",
        # "calories": 1.15,
        "protein": 1.0,
        "carbonate": 1.25,
        "fat": 1.2,
    }
    balance_swing = {
        "name": "Балансовые Качели",
        # "calories": 0.8,
        "protein": 0.9,
        "carbonate": 0.7,
        "fat": 0.5,
    }
    today = date.today().toordinal()
    if _swing_helper(celebrations, today, celebration_swing, diet_day, [17]):
        return celebration_swing
    elif _swing_helper(fetes, today, complex_swing, diet_day, [5,23]):
        return complex_swing
    elif _swing_helper(holidays, today, sugar_swing, diet_day, [11, 29]):
        return sugar_swing
    elif _swing_helper(rituals, today, balance_swing, diet_day, [2,6.8,12,14,18,20,24,26,30]):
        return balance_swing
    return None


def _swing_helper(preset, today, swing, diet_day, days_list):
    if preset:
        if today in preset:
            swing["name"] += " (%s)" % preset[today]
            return swing
    elif diet_day in days_list:
        return swing
    return None


def _get_element(min, max, weight):
    return {
        "mass": {
            "min": int(min),
            "max": int(max),
            },
        "per_kg": {
            "min": int(min * 1000 / weight),
            "max": int(max * 1000 / weight),
            },
        }


if __name__ == '__main__':
    print("170.5", _get_proteins(5, {"muscle_now": 30.6, "weight_now": 170.5, "weight_diff": 170.5/0.888 - 100}, None))
    print("151.5", _get_proteins(5, {"muscle_now": 31.0, "weight_now": 151.5, "weight_diff": 151.5/0.888 - 100}, None))
    print("140.0", _get_proteins(5, {"muscle_now": 31.5, "weight_now": 140.0, "weight_diff": 140.0/0.888 - 100}, None))
    print("130.5", _get_proteins(4, {"muscle_now": 32.0, "weight_now": 130.5, "weight_diff": 130.5/0.888 - 100}, None))
    print("120.5", _get_proteins(4, {"muscle_now": 32.2, "weight_now": 120.5, "weight_diff": 120.5/0.888 - 100}, None))
    print("110.5", _get_proteins(3, {"muscle_now": 32.6, "weight_now": 110.5, "weight_diff": 110.5/0.888 - 100}, None))
    print("100.5", _get_proteins(3, {"muscle_now": 33.5, "weight_now": 100.5, "weight_diff": 100.5/0.888 - 100}, None))
    print("96.5", _get_proteins(2, {"muscle_now": 34.6, "weight_now": 96.5, "weight_diff": 96.5/0.888 - 100}, None))
    print("91.5", _get_proteins(1, {"muscle_now": 35.5, "weight_now": 91.5, "weight_diff": 91.5/0.888 - 100}, None))
    print("88.8", _get_proteins(0, {"muscle_now": 37.5, "weight_now": 88.8, "weight_diff": 88.8/0.888 - 100}, None))
    print("86.5", _get_proteins(-1, {"muscle_now": 30.5, "weight_now": 86.5, "weight_diff": 86.5/0.888 - 100}, None))
    print("80.8", _get_proteins(-2, {"muscle_now": 27.5, "weight_now": 80.8, "weight_diff": 80.8/0.888 - 100}, None))
    print("72.8", _get_proteins(-3, {"muscle_now": 26.5, "weight_now": 72.8, "weight_diff": 72.8/0.888 - 100}, None))
    print("62.8", _get_proteins(-4, {"muscle_now": 25.5, "weight_now": 62.8, "weight_diff": 62.8/0.888 - 100}, None))
    print("52.8", _get_proteins(-5, {"muscle_now": 24.5, "weight_now": 52.8, "weight_diff": 52.8/0.888 - 100}, None))