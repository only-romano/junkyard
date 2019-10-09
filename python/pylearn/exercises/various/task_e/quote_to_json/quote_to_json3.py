#! Программа 'Quote to json'.


def final_library():
    """Рабочий скрипт модуля."""
    text = json_to_text()
    if is_only_library(text) is True:
        # Корневой словарь уникален.
        return simple_library(text)
    else:
        # Корневым объектом является список словарей.
        return several_libraries(text, is_only_library(text))


def json_to_text(file='../quote_to_json2.json'):
    """Открывает файл и преобразует его в список слов."""
    with open(file) as file_json:
        text = file_json.read()
    return text.split()


def is_only_library(text):
    """
    Проверяет, является ли данный словарь единственным элементом списка.
    Если да - возвращает True.  Если нет, возвращает неизвестную границу
    словаря для дальнейшей обработки в функции several_libraries().
    """
    lib_open = 1                        # Колличество '<' в тектсе.
    lib_close = 0                       # Колличество '>' в тексте.
    order = 1                           # Неизвестная граница словаря.
    for word in text[text.index('<')+1:]:
        order += 1
        if word == '<':
            lib_open += 1
        elif word == '>':
            lib_close += 1
            if lib_open == lib_close:   # Цикл обрывается при равенстве
                break                   # открывающих/закрывающих скоб.
    return True if len(text) == order else order


def simple_library(text):
    """
    Обрабатывает одиночные словари.  Возвращает структурированный по
    шаблону словарь после проверки значения ключа 'children' на
    колличество элементов.
    """
    if text.count('<') == 1:
        # Простейший словарь с пустым значением 'children'.
        return {"text": text[text.index('<') + 1], "children": []}
    elif text.count('<') > 1:
        # Составные словари.
        if is_only_library(text[text.index('<') + 1:-1][text.index('<'):]) is True:
            # Словарь с единственным элементом 'children'.
            return {"text": text[1], "children": [simple_library(text[2:-1])]}
        else:
            # Словарь с несколькими элементами ключа 'children'.
            return {"text": text[1],
                    "children": several_libraries(text[2:-1],
                                                  is_only_library(text[2:-1]))}


def several_libraries(text, order):
    """
    Обрабатывает списки словарей.  Возвращает список одиночных словарей
    с помощью границ, полученных из функции is_only_library().
    """
    list_of_libraries = [simple_library(text[:order])]
    if is_only_library(text[order:]) is True:
        list_of_libraries.append(simple_library(text[order:]))
    else:
        list_of_libraries.extend(several_libraries(text[order:],
                                                   is_only_library(text[order:])))
    return list_of_libraries


print(final_library())
