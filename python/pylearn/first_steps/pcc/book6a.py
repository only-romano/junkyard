#! Занятие по книге Python Crash Course, chapter 6, "Dictionaries".
# Занятие первое.

alien_0 = {}
print(alien_0)          # Начинаем с пустой библиотеки.

alien_0[0], alien_0[1], alien_0[2] = {}, {}, {}
alien_0[0]['color'], alien_0[0]['points'] = 'green', 5
alien_0[1]['color'], alien_0[1]['points'] = 'yellow', 10
alien_0[2]['color'], alien_0[2]['points'] = 'red', 15

print(alien_0)          # Добавляем первые связки ' key - value '.

# КЛЮЧ БИБЛИОТЕКИ МОЖЕТ БЫТЬ СПИСКОМ ИЛИ ДРУГОЙ БИБЛИОТЕКОЙ КАК value?

print(alien_0[1]['color'], '\t', alien_0[2]['points'])
print("You just earned " + str(alien_0[2]['points']) + " points!")

# Координаты стартуют обычно из верхнего левого угла.

alien_0[0]['x_position'], alien_0[0]['y_position'] = 0, 25
alien_0[1]['x_position'], alien_0[1]['y_position'] = 20, 25
alien_0[2]['x_position'], alien_0[2]['y_position'] = 50, 35
alien_0[0]['speed'], alien_0[1]['speed'] = 'slow', 'medium'
alien_0[2]['speed'] = 'fast'

# В библиотеках хранение имеет значение относительно доступа не по
# "порядку", а по связке " key - value ".
print(alien_0)          # Eщё связочки ' key - value '.

for alien in alien_0:
    if alien_0[alien]['speed'] == 'slow':
        x_increment = 1
    elif alien_0[alien]['speed'] == 'medium':
        x_increment = 2
    else:
        x_increment = 3
    alien_0[alien]['x_position'] = (alien_0[alien]['x_position'] +
                                    x_increment)

print("Aliens are running!")    # Инопланетяне побежали прочь!

for alien in alien_0:
    print("Alien", alien_0[alien]['color'], "have just moved to",
          alien_0[alien]['x_position'], "!")

# ДАВНО ХОТЕЛ СПРОСИТЬ : МОЖНО ЛИ В КОДЕ ВЕРНУТЬСЯ К ВЫПОЛНЕНИЮ КАКОГО
# НИБУДЬ КОНКРЕТНОГО УЧАСТКА, ЧТО БЫЛ ПРЕЖДЕ?  ТИПА НАПИСАТЬ - ЧТОБЫ
# ВЫПОЛНИИСЬ lines С 31 ПО 38 И ТОЛЬКО ОНИ, КОГДА НАДО ПОСЛЕ УЖЕ
# ВЫПОЛНИТЬ.  ТО ЕСТЬ, Я ПОНИМАЮ, ЧТО МОЖНО ИХ ЗАСУНУТЬ В ОТДЕЛЬНЫЙ
# СКРИПТ И ВЫЗЫВАТЬ КОГДА НАДО.  А МНЕ ИМЕННО ИНТЕРЕСНО - ИЗ ЭТОГО ЖЕ
# КОДА МОЖНО ВЫЗВАТЬ ОТДЕЛЬНЫЕ ВЫШЕЗАПИСАННЫЕ СТРОКИ?