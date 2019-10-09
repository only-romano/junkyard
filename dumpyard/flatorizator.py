import json
from collections import OrderedDict


SUFFIXES = {
    'kz': '_kz',
    'ru': '_ru',
    'en': '_en',
    'kk': '_kk',
}
DOC_ALIASES = OrderedDict({
    '001': 'passport',
    '002': 'udost',
})
DOC_SORT_RULES = OrderedDict({
    '001': lambda it: it.get('endDate', '1'),
    '002': lambda it: it.get('endDate', '1'),
})
ADR_ALIASES = OrderedDict({
    '01': 'timereg',
    '02': 'dep',
})
ADR_SORT_RULES = OrderedDict({
    '01': lambda it: it.get('endDate', '1'),
    '02': lambda it: it.get('beginDate', '1'),
})


def fix_lang_suffix(path: str):
    if len(path) > 2:
        tail = path[-2:]
        return f'{path[:-2]}{SUFFIXES.get(tail, tail)}'
    return path


def flat_general(path, val):
    if type(val) == OrderedDict:
        result = []
        for k, v in val.items():
            result.extend(flat_general(f'{path}_{k}', v))
        return result
    else:
        path = fix_lang_suffix(path.lower())
        return [(path, val)]


def flat_bad_array(path, val, SORT_RULES, ALIASES, bad_name):
    """
    Плоскоризует "плохие массивы". Пример:
      "addressess": {
        "address": [
          ...
        ]
      }
    :param path: из примера это путь_до_него + "addresses"
    :param val: это сам объект лежащий под ключем "addresses"
    :param SORT_RULES: правила сортировки элементов с одинаковым code
    :param ALIASES: читабельные псевдонимы для code
    :param bad_name: из примера это address
    :return: подобное [("addresses_timereg_type_code", "01"), ...]
    """
    result = []
    # Ключ это type.code, а значение это массив документов с таким ключом
    elems_dict = {}
    for elem in val.get(bad_name, []):
        code = elem['type']['code']
        if code in elems_dict:
            elems_dict[code].append(elem)
        else:
            elems_dict[code] = [elem]
    # Сортировка по возрастанию type.code
    elems_dict = OrderedDict(sorted(elems_dict.items(), key=lambda it: it[0]))
    # Сортировка самих массивов и извлечение пар ключ-значение в плоском виде
    for k, v in elems_dict.items():
        v.sort(key=SORT_RULES.get(k, lambda it: it))
        i = 1
        for elem in v:
            index = '' if i == 1 else i
            elem_type = ALIASES.get(k, f'{code}c')
            result.extend(flat_general(f'{path}_{elem_type}{index}', elem))
            i += 1

    return result


def safe_call(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except BaseException as ex:
        print(str(ex))
        return []


def flat_gbdfl_person(person: OrderedDict):
    """
    Точка входа в модуль.
    Превращает древовидную структуру gbdfl_person в плоскую для geonomics-а
    :param person: разветвленная структура пришедшая из gbdfl
    :return: плоская структура, не имеющая вложений
    """
    flated_person = OrderedDict()
    for key, value in person.items():
        if key == 'documents':
            rows = safe_call(flat_bad_array, key, value,
                             DOC_SORT_RULES, DOC_ALIASES, 'document')
        elif key == 'addresses':
            rows = safe_call(flat_bad_array, key, value,
                             ADR_SORT_RULES, ADR_ALIASES, 'address')
        else:
            rows = safe_call(flat_general, key, value)
        flated_person.update(rows)

    return flated_person
