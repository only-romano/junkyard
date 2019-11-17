# Helpful tools for slots app
from diet_patterns import DIET


def is_smoked(slots):
    no = input("Вы курили вчера? (оставьте пустым если да) \n")
    if no:
        slots.smoke += 1
    else:
        print("И зря")
        slots.smoke = 0
    return { "smoke": slots.smoke }


def weight_and_things(slots):
    weight = _get_value("Вы измеряли свой вес? Если да, то введи значение: ")
    slots.weight.append(weight)
    muscle = _get_value("А мышцы измеряли? ")
    slots.muscle.append(muscle)
    fat = _get_value("Что насчёт жира? Есть цифферки? ")
    slots.fat.append(fat)
    water = _get_value("Ну и наконец - вода: ")
    slots.water.append(water)
    diet_done = True if input("Придерживались диеты? Если да, то введи что-то: ") else False
    slots.diet_done.append(diet_done)
    good_things = []
    for x in _get_iter("Делали что-то хорошее? (напишите что, если да) "):
        good_things.append(x)
    slots.good_things.extend(good_things)
    new_things = []
    for x in _get_iter("Узнали что-то новое? (напишите что, если да) "):
        new_things.append(x)
    slots.new_things.extend(new_things)
    diet = DIET(slots)
    slots.diet.append(diet)
    return {
        "weight": weight,
        "muscle": muscle,
        "fat": fat,
        "water": water,
        "diet_done": diet_done,
        "diet": diet,
        "good_things": good_things,
        "new_things": new_things,
        }


# internal use function
def _get_iter(text):
    thing = input(text)
    while thing:
        yield thing
        thing = input(text)


def _get_value(text):
    try:
        return float(input(text).replace(',', '.'))
    except ValueError:
        return None
