# Helpful tools for slots app
import re
from datetime import date
from diet_patterns import DIET


def weight_and_things(slots):
    yesterday = _load_yesterday_file()
    # weight's params
    weight = _operate_weight(slots, yesterday)
    muscle = _operate_muscle(slots, yesterday)
    fat = _operate_fat(slots, yesterday)
    water = _operate_water(slots, yesterday)
    # things params
    good_things = _operate_good_things(slots, yesterday)
    new_things = _operate_new_things(slots, yesterday)
    # diet params
    diet_done = _operate_diet_done(slots, yesterday)
    diet = DIET(slots)
    # etc params
    smoke = _operate_smoke(slots, yesterday)
    # return object
    return {
        "weight": weight,
        "muscle": muscle,
        "fat": fat,
        "water": water,
        "good_things": good_things,
        "new_things": new_things,
        "diet_done": diet_done,
        "diet": diet,
        "smoke": smoke,
        }


# internal use function
def _load_yesterday_file():
    filename = "day_files/day_file_%s.md" % str(_yesterday()).replace('-', '_')
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None


def _yesterday():
    return date.fromordinal(date.today().toordinal()-1)


def _operate_weight(slots, file):
    return _operate(slots.weight, file,
        pattern=r"Мой вес[ ]*:[ |_]*(\d+[\.|,]?\d*)[ |_]*кГ",
        question="Вы вчера измеряли свой вес? Если да, то введите значение: "
        )


def _operate_muscle(slots, file):
    return _operate(slots.muscle, file,
        pattern=r"Мои мышцы[ ]*:[ |_]*(\d+[\.|,]?\d*)[ |_]*кГ",
        question="А мышцы измеряли? Введите значение, если да: "
        )


def _operate_fat(slots, file):
    return _operate(slots.fat, file,
        pattern=r"Мой жир[ ]*:[ |_]*(\d+[\.|,]?\d*)[ |_]*%",
        question="Что насчёт жира? Есть цифферки? "
        )


def _operate_water(slots, file):
    return _operate(slots.water, file,
        pattern=r"Моя вода[ ]*:[ |_]*(\d+[\.|,]?\d*)[ |_]*%",
        question="Ну и наконец - вода, измеряли? Значение, если есть: "
        )


def _operate(slots, file, pattern, question):
    result = None
    if file:
        search = re.search(pattern, file)
        if search:
            result = _get_value(result=search[1])
    result = result or _get_value(text=question)
    slots.append(result)
    return result


def _operate_good_things(slots, file):
    return _operate_iter(slots.good_things, file,
        pat_st=r"Сегодня вы сделали хорошего:\n",
        pat_in=r"[ |\t]*\d[ |_]*(.*)\n",
        pat_end = r"\n\n",
        question="Делали что-то хорошее? (напишите что, если да) ")


def _operate_new_things(slots, file):
    return _operate_iter(slots.new_things, file,
        pat_st=r"Сегодня вы узнали и выучили новое:\n",
        pat_in=r"[ |\t]*\d[ |_]*(.*)\n",
        pat_end = r"\n\n",
        question="Узнали что-то новое? (напишите что, если да) ")


def _operate_iter(slots, file, pat_st, pat_in, pat_end, question):
    result = None
    if file:
        try:
            index_st = re.search(pat_st, file).span()[1]
            file = file[index_st:]
            index_end = re.search(pat_end, file).span()[0]
            file = file[:index_end+1]
            find = re.search(pat_in, file)
            result = []
            while find:
                result.append(find[1].strip())
                file = file[find.span()[1]:]
                find = re.search(pat_in, file)
        except Exception:
            pass
    if not result:
        result = []
        for x in _get_iter(question):
            result.append(x)
    slots.extend(result)
    return result


def _operate_diet_done(slots, file):
    result = None
    if file:
        search = re.search(r"Я придерживался диеты:[ |_|\t]*(.*)\n", file)
        if search:
            result = search[1].lower().replace(' ', '').replace('_', '').replace('\t', '')
    if result:
        result = result.replace('-', '').replace('нет', '').replace('no', '').replace('курю', '')
    else:
        result = input("Придерживались диеты? Если да, то введи что-то: ")
    result = len(result) > 0
    if result:
        slots.diet_done += 1
    else:
        slots.diet_done = 0
    return slots.diet_done


def _operate_smoke(slots, file):
    result = None
    if file:
        search = re.search(r"Я сегодня не курил:[ |_|\t]*(.*)\n", file)
        if search:
            result = search[1].lower().replace(' ', '').replace('_', '').replace('\t', '')
    if result:
        result = result.replace('-', '').replace('нет', '').replace('no', '').replace('курю', '')
    else:
        result = input("Вы курили вчера? (оставьте пустым если да): ")
    result = len(result) > 0
    if result:
        slots.smoke += 1
    else:
        slots.smoke = 0
    return slots.smoke


def _get_value(text=None, result=None):
    try:
        if text:
            return float(input(text).replace(',', '.'))
        if result:
            return float(result.replace(',', '.'))
    except ValueError:
        pass
    return None


def _get_iter(text):
    thing = input(text)
    while thing:
        yield thing
        thing = input(text)


if __name__ == '__main__':
    index = re.search(r"Сегодня вы сделали хорошего:\n",
        "Сегодня вы сделали хорошего:\n11221222   \n  \n\n")
    n = re.search(r"Сегодня вы сделали хорошего:\n((.*)|\n)*\n\n",
        "Сегодня вы сделали хорошего:\n11221222   \n  \n\n")
    #print(index[1])
