from tkinter import *
from random import randint, choice

def bAaction():
    print("Thanks")


def bBaction():
    print("It hurts so much.")


def roll():
    text.delete(0.0, END)
    text.insert(END, str(randint(1, 6)))


window = Tk()
buttonA = Button(window, text='Press!', command=bAaction)
buttonB = Button(window, text='Don\'t press', command=bBaction)
buttonA.pack()
buttonB.pack()

text = Text(window, width=1, height=1)
buttonC = Button(window, text="Press to roll the die!", command=roll)
text.pack()
buttonC.pack()

size = 500
canvas = Canvas(window, width=size, height=size)
canvas.pack()

while True:
    col = choice(['pink', 'orange', 'purple', 'yellow'])
    x0 = randint(0, size)
    y0 = randint(0, size)
    d = randint(0, size/5)
    canvas.create_oval(x0, y0, x0 + d, y0 + d, fill=col)
    window.update()

window.mainloop()
