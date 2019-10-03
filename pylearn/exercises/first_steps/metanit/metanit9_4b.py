#! Работа с материалами Metanit, глава 9, часть 4.  "Позиционирование
# элементов".  Занятие 2.

from tkinter import *

# Используем параметр side:

root = Tk()
root.title("Gui на Python")
root.geometry("300x250")

btn1 = Button(text="BOTTOM", background="#555", foreground="#ccc",
              padx="15", pady="6", font="Verdana 15")
btn1.pack(side=BOTTOM)

btn2 = Button(text="RIGHT", background="#555", foreground="#ccc",
              padx="15", pady="6", font="15")
btn2.pack(side=RIGHT, fill=Y)

btn3 = Button(text="LEFT", background="#555", foreground="#ccc",
              padx="15", pady="6", font="15")
btn3.pack(side=LEFT, fill=Y)

btn4 = Button(text="TOP", background="#555", foreground="#ccc",
              padx="15", pady="6", font="15")
btn4.pack(side=TOP)

root.mainloop()
