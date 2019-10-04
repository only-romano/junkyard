#! Работа с материалами Metanit, глава 9, часть 9.  "Listbox".
# Часть вторая.

from tkinter import *

# Основные методы Listbox:
#  ..  curselection(): возвращает набор индексов выделенных элементов.
#  ..  delete(first, last = None): удаляет элементы с индексами из
#      диапазона [first, last].  Если второй параметр опущен, то
#      удаляет только один элемент по индексу first.
#  ..  get(first, last = None): возвращает кортеж, который содержит
#      текст элементов с индексами из дипазона [first, last].  Если
#      второй параметр опущен, возвращается только текст элемента с
#      индексом first.
#  ..  insert(index, element): вставляет элемент по определенному индексу.
#  ..  size(): возвращает количество элементов.


# Удаление выделенного элемента
def delete():
    selection = languages_listbox.curselection()
    # мы можем получить удаляемый элемент по индексу
    # selected_language = languages_listbox.get(selection[0])
    languages_listbox.delete(selection[0])
# Kнопка по нажатию удаляет выделенный элемент.  Для этого мы сначала
# получаем выделенные индексы через метод curselection().  Так как в
# нашем случае выделяется только один элемент, то получаем его индекс
# через выражение selection[0].  И этот индекс передаем в метод delete()
# для удаления.


# Добавление нового элемента
def add():
    new_language = language_entry.get()
    languages_listbox.insert(0, new_language)
# Kнопка вызывает функцию add(), которая получает введенное в
# текстовое поле значение и добавляет его на первое место в списке с
# помощью метода insert().


root = Tk()
root.title("Путь к калькулятору")

# Текстовое поле и кнопка для добавления в список
language_entry = Entry(width=40)
language_entry.grid(column=0, row=0, padx=6, pady=6)
add_button = Button(text="Добавить", command=add).grid(column=1, row=0,
                                                       padx=6, pady=6)

# Создаём список
languages_listbox = Listbox()
languages_listbox.grid(row=1, column=0, columnspan=2, sticky=W+E,
                       padx=5, pady=5)

# Добавляем в список начальные элементы
languages_listbox.insert(END, "Python")
languages_listbox.insert(END, "C#")

delete_button = Button(text="Удалить", command=delete).grid(row=2, column=1,
                                                            padx=5, pady=5)

root.mainloop()
