'''
Очень интересно конечно что получиться :) какую функцию ты напишешь.
Сохрани скрины промежуточные, Пазялюста )) 
'''

def get_ch_list(ls):
    ns = ls[:]
    es = []
    for i in ns:
        es.append(i)
        ns.remove(i)
    c = 0
    while ns != []:
        sys = ns.pop(0)
        es.insert(c, sys)
        c +=2
    return es

def test_equals(arg, value):
    print(f'Аргумент: {arg}, '
          f'ожидание: {value} |-> '
          f'результат: {get_ch_list(arg)},')


# Тесты
try:
    test_equals([], [])
    test_equals([1], [1])
    test_equals([1, 2], [2, 1])
    test_equals([1, 2, 3], [2, 1, 3])
    test_equals([1, 2, 3, 4, 5], [2, 1, 4, 3, 5])
    test_equals([1, 2, 3, 4, 5, 6], [2, 1, 4, 3, 6, 5])
    test_equals("Катя", "Катя")
except Exception as e:
    print(e)