from tkinter import *


def move_triangle(event):
    key = event.keysym
    if key == "Up":
        canvas.move(play, 0, -3)
    elif key == "Down":
        canvas.move(play, 0, 3)
    elif key == "Left":
        canvas.move(play, -3, 0)
    elif key == "Right":
        canvas.move(play, 3, 0)
    elif key == "S":
        canvas.itemconfig(play, fill="blue")
    elif key == "Y":
        canvas.itemconfig(play, fill="black")
    elif key == "s":
        canvas.itemconfig(play, outline="blue")
    elif key == "y":
        canvas.itemconfig(play, outline="black")

window = Tk()

canvas = Canvas(window, width=400, height=400)
canvas.pack()

play = canvas.create_polygon(10, 10, 10, 60, 50, 35)

canvas.bind_all('<KeyPress>', move_triangle)

window.mainloop()
