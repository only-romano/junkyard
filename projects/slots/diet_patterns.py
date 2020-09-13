from datetime import date
from math import ceil
from print_patterns import notes
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
    weight_now = next(
        (w for w in reversed(slots.weight) if w is not None), 155.0)
    muscle_now = next(
        (m for m in reversed(slots.muscle) if m is not None), 30.0)
    fat_now = next(
        (f for f in reversed(slots.fat) if f is not None), 35.0)
    water_now = next(
        (w for w in reversed(slots.water) if w is not None), 45.0)

    diff = (weight_now / MVP['weight'] * 100 - 100)
    sign = -1 if diff < 0 else 1
    if diff <= -30 or diff >= 50:
        stage_number = sign * 5
    elif diff <= -20 or diff >= 25:
        stage_number = sign * 4
    elif abs(diff) >= 5:
        stage_number = sign * (3 if abs(diff) >= 10 else 2)
    else:
        stage_number = sign * 1 if abs(diff) >= 1.75 else 0

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
        "weight": 88.8,
        "muscle": 40.0,
        "fat": 7.0,
        "water": 57.5,
        }


# internal use functions
def _diet_text(stage):
    s = stage
    d_min, d_med, d_max = 'date_min', 'date_med', 'date_max'
    return "\t\tДиета на сегодня. " + "\n\t\t\t".join([
        "СТАДИЯ № %i\n" % abs(s['number']), s['sport'], s['description'] + "\n",
        "ПОКАЗАТЕЛИ:     %.1f - %.1f кГ" % (s['weight_min'], s['weight_max']),
        "РАСЧЁТН. ВРЕМЯ: %s ... (%s) ... %s" % (s[d_min], s[d_med], s[d_max]),
                "%s" % ("\n\t\t\t" + s['swing'] + "\n" if s['swing'] else ""),
        _get_element_value("БЕЛОК:", s['protein']),
        _get_element_value("САХАР:", s['carbonate']),
        _get_element_value("ЖИРЫ: ", s['fat']) + "\n",
        "ККАЛ:    %4i - %4i ККал" % (s['calories']['min'], s['calories']['max']),
        "ВОДА:    %4i - %4i мл\n\n" % (s['water']['min'], s['water']['max']),
        "СЕГОДНЯ Я КУШАЛ:" + _today_pcf() + notes(10, True) + "\n",
    ])


def _stage_constructor(stage_number, values):
    nutrients = _get_nutrients(stage_number, values)
    sn, wi = stage_number, "weight_ideal"
    return {
        "number": stage_number,
        "sport": _get_sport_rate_description(abs(stage_number)),
        "description": _get_stage_description(stage_number),
        "weight_min": _get_stage_min_weight(stage_number, values[wi]),
        "weight_max": _get_stage_max_weight(stage_number, values[wi]),
        "date_min": _get_stage_min_date(sn, values['weight_diff'], values[wi]),
        "date_med": _get_stage_med_date(sn, values['weight_diff'], values[wi]),
        "date_max": _get_stage_max_date(sn, values['weight_diff'], values[wi]),
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
    h, t, m = " ВЕСА С ПОМОЩЬЮ ", " НАГРУЗОК ", " МЫШЕЧНОЙ МАССЫ"
    c, g, l, s0 = "КОРРЕКЦИЯ", "НАБОР", "СБРОС", "ОПТИМАЛЬНОЙ РАБОТЫ ОРГАНИЗМА"
    if stage_number == 0:
        return f"ПРАВИЛЬНОЕ ПИТАНИЕ И ПОДДЕРЖИВАЮЩИЕ НАГРУЗКИ ДЛЯ {s0}"
    elif stage_number == -1:
        return f"{c+h}ПОВЫШЕННИЯ РАЦИОНА И МАКСИМАЛЬНЫХ{t}С {g}ОМ{m}"
    elif stage_number == 1:
        return f"{c+h}ПРАВИЛЬНОГО ПИТАНИЯ И МАКСИМАЛЬНЫХ{t}С {g}ОМ{m}"
    elif stage_number == -2:
        return f"{c+h}УВЕЛИЧЕННОГО РАЦИОНА И ВЫСОКИХ{t}С {g}ОМ{m}"
    elif stage_number == 2:
        return f"{c+h}ОГРАНИЧЕННОГО ПИТАНИЯ И ВЫСОКИХ{t}С МИНИМАЛЬНЫМ {g}ОМ{m}"
    elif stage_number == -3:
        return f"{g+h}ОБИЛЬНОГО РАЦИОНА И УСИЛЕННЫХ{t}С {g}ОМ{m}"
    elif stage_number == 3:
        return f"{l+h}ТОЛЕРАНТНОЙ ДИЕТЫ И УСИЛЕННЫХ{t}БЕЗ ПОТЕРЬ{m}"
    elif stage_number == -4:
        return f"{g+h}ОБИЛЬНОГО РАЦИОНА И СРЕДНИХ{t}С МИНИМАЛЬНЫМ {g}ОМ{m}"
    elif stage_number == 4:
        return f"{l+h}ДИЕТЫ И СРЕДНИХ{t}С МИНИМАЛЬНЫМИ ПОТЕРЯМИ{m}"
    elif stage_number == -5:
        return f"{g+h}ОБИЛЬНОГО РАЦИОНА И МИНИМАЛЬНЫХ{t}БЕЗ {g}А{m}"
    elif stage_number == 5:
        return f"{l+h}ЖЁСТКОЙ ДИЕТЫ И МИНИМАЛЬНЫХ{t}С ПОТЕРЕЙ{m}"
    # return "%s ВЕСА С ПОМОЩЬЮ %s НАГРУЗОК %s МЫШЕЧНОЙ МАССЫ"
    # % (weight, diet_sport, muscle)


def _get_stage_min_weight(stage_number, ideal_weight):
    if stage_number == 0: coef = 0.9825
    elif stage_number == 1: coef = 1.0175
    elif stage_number == 2: coef = 1.05
    elif stage_number == 3: coef = 1.10
    elif stage_number == 4: coef = 1.25
    elif stage_number == 5: coef = 1.50
    elif stage_number == -1: coef = 0.95
    elif stage_number == -2: coef = 0.90
    elif stage_number == -3: coef = 0.80
    elif stage_number == -4: coef = 0.70
    elif stage_number == -5: coef = 0.50
    # return
    return ideal_weight * coef + (0 if stage_number > 0 else 0.1)


def _get_stage_max_weight(stage_number, ideal_weight):
    if stage_number == 0: coef = 1.0175
    elif stage_number == 1: coef = 1.05
    elif stage_number == 2: coef = 1.10
    elif stage_number == 3: coef = 1.25
    elif stage_number == 4: coef = 1.50
    elif stage_number == 5: coef = 2.00
    elif stage_number == -1: coef = 0.9825
    elif stage_number == -2: coef = 0.95
    elif stage_number == -3: coef = 0.90
    elif stage_number == -4: coef = 0.80
    elif stage_number == -5: coef = 0.70
    # return
    return ideal_weight * coef - (0 if stage_number < 0 else 0.1)


def _get_stage_min_date(stage_number, weight_diff, ideal_weight):
    if        stage_number   ==  0:  return ""
    elif  abs(stage_number)  ==  1:  stage_coef =  1.75
    elif  abs(stage_number)  ==  2:  stage_coef =  5
    elif  abs(stage_number)  ==  3:  stage_coef = 10
    elif      stage_number   ==  4:  stage_coef = 25
    elif      stage_number   ==  5:  stage_coef = 50
    elif      stage_number   == -4:  stage_coef = 20
    elif      stage_number   == -5:  stage_coef = 30
    else:     return ""
    # return
    diff = abs(weight_diff)
    coef = ceil((diff-stage_coef) * (ideal_weight/abs(stage_number))**0.5)
    return date.fromordinal(date.today().toordinal()+coef).strftime("%d %b %Y")


def _get_stage_med_date(stage_number, weight_diff, ideal_weight):
    if stage_number == 0: return "ИДЕАЛ"
    return _get_stage_min_date(stage_number, weight_diff, ideal_weight*2)


def _get_stage_max_date(stage_number, weight_diff, ideal_weight):
    return _get_stage_min_date(stage_number, weight_diff, ideal_weight*4)


def _get_nutrients(stage_number, values):
    swing      =  _get_swing(values['diet_day'])
    proteins   =  _get_proteins(stage_number, values, swing)
    carbonates =  _get_carbonates(stage_number, values, swing)
    fats       =  _get_fats(stage_number, values, swing)
    calories   =  _get_calories(proteins, carbonates, fats)

    proteins['procent']   = proteins['mass']['max'] * 420 / calories['max']
    carbonates['procent'] = carbonates['mass']['max'] * 420 / calories['max']
    fats['procent']       = fats['mass']['max'] * 930 / calories['max']

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
    min_coef    = 1.65 - abs(values['weight_diff'])*0.015
    min_coef    = min_coef if min_coef >= 0.4 else 0.4
    max_coef    = 2.35 - abs(values['weight_diff'])*0.027
    max_coef    = max_coef if max_coef >= 0.45 else 0.45
    p_min       = values['weight_now'] * (min_coef - muscle_diff*0.01)
    p_max       = values['weight_now'] * (max_coef - muscle_diff*0.02)
    if swing:
        p_min *= swing['protein']
        p_max *= swing['protein']
    return _get_element(p_min, p_max, values['weight_now'])


def _get_carbonates(stage_number, values, swing):
    wd = values['weight_diff']
    diff = wd if wd > 0 else wd/4
    fat_mass = (values['fat_now'] - MVP['fat']) * values['weight_now'] / 100
    min_coef = 3.5 - diff*(0.04 if stage_number < 5 else 0.035)
    max_coef = 4.5 - diff*(0.05 if stage_number < 5 else 0.04)
    min_coef = min_coef if min_coef >= 0.75 else 0.75
    max_coef = max_coef if max_coef >= 1.25 else 1.25
    if stage_number < 1:
        max_coef += 1
    c_min = values['weight_now'] * (min_coef - fat_mass * (0.0075 if stage_number < 5 else 0.006))
    c_max = values['weight_now'] * (max_coef - fat_mass * (0.015 if stage_number < 5 else 0.01))
    if c_min > c_max:
        c_min, c_max = c_max, c_min
    if swing:
        c_min *= swing['carbonate']
        c_max *= swing['carbonate']
    return _get_element(c_min, c_max, values['weight_now'])


def _get_fats(stage_number, values, swing):
    wd = values['weight_diff']
    fat_mass = (values['fat_now'] - MVP['fat']) * values['weight_now'] / 100
    if fat_mass > 50:
        fat_mass = 50
    diff = wd if wd > 0 else wd/4
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
    bs, dd = balance_swing, diet_day
    if _swing_helper(celebrations, today, celebration_swing, diet_day, [17]):
        return celebration_swing
    elif _swing_helper(fetes, today, complex_swing, diet_day, [5,23]):
        return complex_swing
    elif _swing_helper(holidays, today, sugar_swing, diet_day, [11, 29]):
        return sugar_swing
    elif _swing_helper(rituals, today, bs, dd, [3,6,9,12,15,18,21,24,28]):
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


def _today_pcf():
    return f"{29 * ' '}(Б: _____   C: _____   Ж: _____)"


# exported values
__all__ = ['DIET', 'get_MVP']


if __name__ == '__main__':
    G, f, n, d = _get_fats, "fat_now", "weight_now", "weight_diff"
    print("170.5", G( 5, {f: 35.6,  n: 170.5,  d: 170.5/0.888 - 100},  None))
    print("151.5", G( 5, {f: 32.0,  n: 151.5,  d: 151.5/0.888 - 100},  None))
    print("140.0", G( 5, {f: 30.5,  n: 140.0,  d: 140.0/0.888 - 100},  None))
    print("130.5", G( 4, {f: 29.0,  n: 130.5,  d: 130.5/0.888 - 100},  None))
    print("120.5", G( 4, {f: 27.2,  n: 120.5,  d: 120.5/0.888 - 100},  None))
    print("110.5", G( 3, {f: 25.6,  n: 110.5,  d: 110.5/0.888 - 100},  None))
    print("100.5", G( 3, {f: 21.5,  n: 100.5,  d: 100.5/0.888 - 100},  None))
    print("96.5",  G( 2, {f: 19.6,  n: 96.5,   d: 96.5/0.888 - 100},   None))
    print("91.5",  G( 1, {f: 17.5,  n: 91.5,   d: 91.5/0.888 - 100},   None))
    print("88.8",  G( 0, {f: 15.5,  n: 88.8,   d: 88.8/0.888 - 100},   None))
    print("86.5",  G(-1, {f: 13.5,  n: 86.5,   d: 86.5/0.888 - 100},   None))
    print("80.8",  G(-2, {f: 11.5,  n: 80.8,   d: 80.8/0.888 - 100},   None))
    print("72.8",  G(-3, {f: 9.5,   n: 72.8,   d: 72.8/0.888 - 100},   None))
    print("62.8",  G(-4, {f: 7.5,   n: 62.8,   d: 62.8/0.888 - 100},   None))
    print("52.8",  G(-5, {f: 5.5,   n: 52.8,   d: 52.8/0.888 - 100},   None))
