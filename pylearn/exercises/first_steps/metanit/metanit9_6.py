#! Работа с материалами Metanit, глава 9, часть 6.  "Поле ввода Entry".

# Элемент Entry представляет поле для ввода текста.  Конструктор Entry
# принимает следующие параметры:

# Entry(master, options)

# Где master - ссылка на родительское окно, options - набор параметров:
#  ..  bg: фоновый цвет.
#  ..  bd: толщина границы.
#  ..  cursor: курсор указателя мыши при наведении на текстовое поле.
#  ..  fg: цвет текста.
#  ..  font: шрифт текста.
#  ..  justify: устанавливает выравнивание текста. Значение LEFT
#      выравнивает текст по левому краю, CENTER - по центру, RIGHT - по
#      правому краю.
#  ..  relief: определяет тип границы, по умолчанию значение FLAT.
#  ..  selectbackground: фоновый цвет выделенного куска текста.
#  ..  selectforeground: цвет выделенного текста.
#  ..  show: задает маску для вводимых символов.
#  ..  state: состояние элемента, может принимать значения NORMAL
#      (поумолчанию) и DISABLED.
#  ..  textvariable: устанавливает привязку к элементу StringVar.
#  ..  width: ширина элемента.

# Определим элемент Entry:

from tkinter import *
from tkinter import messagebox

# Методы Entry:
#  ..  insert(index, str): вставляет в текстовое поле строку по
#      определенному индексу.
#  ..  get(): возвращает введенный в текстовое поле текст.
#  ..  delete(first, last=None): удаляет символ по индексу first.
#      Если указан параметр last, то удаление производится до индекса
#      last.  Чтобы удалить до конца, в качестве второго параметра
#      можно использовать значение END.


def display_full_name():
    """Посылает нахуй"""
    messagebox.showinfo("Нахуй 2018!", name.get() + " " +
                        surname.get() + ", " + message.get() + ".")
    # Для вывода сообщения здесь применяется дополнительный модуль
    # messagebox, содержащий функцию showinfo(), которая и выводит
    # введенный в текстовое поле текст.


def clear():
    name_entry.delete(0, END)
    surname_entry.delete(0, END)
    message_entry.delete(0, END)


root = Tk()
root.title("Посылатель нахуй 2018")

message = StringVar()
name = StringVar()
surname = StringVar()

# Hеобязательно обращаться к тексту в Entry через переменные типа
# StringVar, мы можем это сделать напрямую через метод get.

name_label = Label(text="Введите имя:")
surname_label = Label(text="Введите фамилию:")
message_label = Label(text="Введите своё послание этому человеку:")

name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=1, column=0, sticky="w")
message_label.grid(row=2, column=0, sticky="w")

name_entry = Entry(textvariable=name)
surname_entry = Entry(textvariable=surname)
message_entry = Entry(textvariable=message)

name_entry.grid(row=0, column=1, padx=5, pady=5)
surname_entry.grid(row=1, column=1, padx=5, pady=5)
message_entry.grid(row=2, column=1, padx=5, pady=5)

# Значения по умолчанию.
name_entry.insert(0, "Jessica")
surname_entry.insert(0, "Alba")
message_entry.insert(0, "FUCK YOU !")

message_button = Button(text="НАХУЙ !", command=display_full_name)
display_button = Button(text="Clear", command=clear)

message_button.grid(row=3, column=1, padx=5, pady=5, sticky="w")
display_button.grid(row=3, column=1, padx=5, pady=5, sticky="e")

root.mainloop()
