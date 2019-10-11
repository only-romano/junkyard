#! Работа с материалами Metanit, глава 9, часть 9.  "Listbox".
# Часть первая.

from tkinter import *

# Элемент Listbox в tkinter представляет список объектов.

languages = ["Python", "JavaScript", "C#", "Java", "C/C++", "Swift",
             "PHP", "Visual Basic.NET", "F#", "Ruby", "Rust", "R", "Go",
             "T-SQL", "PL-SQL", "Typescript"]

root = Tk()
root.title("Путь к калькулятору")

# Для настройки виджета Listbox мы можем указать в его конструкторе
# следующие параметры:
#  ..  bg: фоновый цвет.
#  ..  bd: толщина границы вокруг элемента.
#  ..  cursor: курсор при наведении на Listbox.
#  ..  font: настройки шрифта.
#  ..  fg: цвет текста.
#  ..  height: высота элемента в строках. По умолчанию 10 строк.
#  ..  highlightcolor: цвет элемента, когда он получает фокус.
#  ..  highlightthickness: толщина границы элемента, когда он
#      находится в фокусе.
#  ..  relief: устанавливает стиль элемента, по умолчанию имеет
#      значение SUNKEN.
#  ..  selectbackground: фоновый цвет для выделенного элемента.
#  ..  selectmode: определяет, сколько элементов могут быть выделены.
#      Может принимать значения: BROWSE, SINGLE, MULTIPLE, EXTENDED.
#      Например, если необходимо включить множественное выделение
#      элементов, то можно использовать значения MULTIPLE или EXTENDED..
#  ..  width: устанавливает ширину элемента в символах. По умолчанию
#      ширина - 20 символов.
#  ..  xscrollcommand: задает горизонтальную прокрутку.
#  ..  yscrollcommand: устанавливает вертикальную прокрутку.

# Некоторую сложность при использовании Listbox представляет создание
# прокрутки.  Рассмотрим, как это сделать:

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Для создания прокрутки создается элемент Scrollbar.  И так как
# необходимо прокручивать listbox по вертикали, то у него задается
# параметр yscrollcommand=scrollbar.set.

languages_listbox = Listbox(yscrollcommand=scrollbar.set, width=40)

for language in languages:
    languages_listbox.insert(END, language)

# В конце scrollbar ассоциируется с функцией, которую надо выполнять
# при прокрутке.  В данном случае это метод yview элемента listbox.

languages_listbox.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=languages_listbox.yview)

root.mainloop()
