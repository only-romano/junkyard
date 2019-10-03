from tkinter import *
import random


def i_miss_you():
    print("Я скучаю по тебе")


def person(width, height):
    print("Моя ширина - %s, а высота - %s" % (width, height))


def random_rectangle(width, height, fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)


person(height=3, width=4)
print('%x' % 15)  # вывод в 16-ричной системе
print('%02x' % 15)  # форматированный вывод в 16-ричной системе

window = Tk()

btn = Button(window, text="Нажми меня", command=i_miss_you)
btn.pack()
canvas = Canvas(window, width=500, height=500)
canvas.pack()


canvas.create_line(0, 0, 500, 500)
canvas.create_rectangle(10, 10, 50, 50)
canvas.create_rectangle(100, 10, 300, 50)
canvas.create_rectangle(450, 10, 400, 300)

random_rectangle(400, 400, 'green')

colors = ["green", "red", "blue", "orange", "yellow", "pink", "purple", "violet", "magenta", "cyan", "#ffd800"]

for x in range(100):
    color = random.randint(0, len(colors) - 1)
    random_rectangle(400, 400, colors[color])

window.mainloop()
