#! Работа с материалами Metanit, глава 9, часть 8.  "Radiobutton".

from tkinter import *

languages = [('Sexy', 1), ('Girls', 2), ('Dicks', 3), ('Pussies', 4)]


def select():
    l = language.get()
    if l == 1:
        sel.config(text="You're sexy!")
    elif l == 2:
        sel.config(text="Choosed girls")
    elif l == 3:
        sel.config(text="Suck dicks")
    elif l == 4:
        sel.config(text="Rub pussies")


root = Tk()
root.title("Путь к калькулятору")
root.geometry("300x250")

header = Label(text="Choose direction", padx=15, pady=10)
header.grid(row=0, column=0, sticky=W)

language = IntVar()

# Параметры Radiobutton:
#  ..  activebackground: фоновый цвет переключателя в нажатом состоянии.
#  ..  activeforeground: цвет текста переключателя в нажатом состоянии.
#  ..  bg: фоновый цвет переключателя.
#  ..  bitmap: монохромное изображение для переключателя.
#  ..  borderwidth: граница вокруг переключателя.
#  ..  command: ссылка на функцию, которая вызывается при нажатии на
#      переключатель.
#  ..  cursor: курсор при наведении на элемент.
#  ..  font: шрифт.
#  ..  fg: цвет текста.
#  ..  height: высота элемента в строках текста.  По умолчанию равно 1.
#  ..  image: графическое изображение, отображаемое на элементе.
#  ..  justify: выравнивание текста, принимает значения CENTER, LEFT,
#      RIGHT.
#  ..  padx: отступы справа и слева от текста до границы переключателя.
#  ..  pady: отступы сверху и снизу от текста до границы переключателя.
#  ..  relief: стиль переключателя, по умолчанию имеет значение FLAT.
#  ..  selectcolor: цвет кружка переключателя.
#  ..  selectimage: изображение на переключателе, когда он находится
#      в отмеченном состоянии.
#  ..  state: состояние элемента, может принимать значения NORMAL
#      (по умолчанию), DISABLED и ACTIVE.
#  ..  text: текст элемента..
#  ..  textvariable: устанавливает привязку к переменной StringVar,
#      которая задает текст переключателя.
#  ..  underline: индекс подчеркнутого символа в тексте элемента.
#  ..  variable: ссылка на переменную, как правило, типа IntVar,
#      которая хранит состояние переключателя.
#  ..  value: значение переключателя.
#  ..  width: ширина элемента.
#  ..  wraplength: устанавливает перенос символов на другую строку в
#      тексте элемента.

row = 1
for txt, val in languages:
    Radiobutton(text=txt, value=val, variable=language, padx=15, pady=10,
                command=select).grid(row=row, sticky=W)
    row += 1

# Здесь определены два переключателя, но оба они привязаны к одной
# переменной IntVar.  При этом они имеют разные значения,
# устанавливаемые через параметр value. Поэтому при включении одного
# переключателя, другой перейдет в неотмеченное состояние.

sel = Label(padx=15, pady=10)
sel.grid(row=row, sticky=W)

root.mainloop()
