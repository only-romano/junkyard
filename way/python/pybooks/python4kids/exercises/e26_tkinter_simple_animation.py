import time
from tkinter import *


def move_play(x, y=0):
    for i in range(60):
        canvas.move(play, x, y)
        window.update()
        time.sleep(0.02)


window = Tk()

canvas = Canvas(window, width=400, height=400)
canvas.pack()
play = canvas.create_polygon(10, 10, 10, 60, 50, 35)

move_play(5)
move_play(-5)
move_play(5, 5)
move_play(-5, -5)
