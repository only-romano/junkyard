from tkinter import *
from time import time, sleep

window = Tk()
window.attributes('-topmost', 1)
window.title("Alien")
c = Canvas(window, height=300, width=400)
c.pack()

body = c.create_oval(100, 150, 300, 250, fill='green')
eye = c.create_oval(170, 70, 230, 130, fill='white')
eyeball = c.create_oval(190, 90, 210, 110, fill='black')
mouth = c.create_oval(150, 220, 250, 240, fill='red')
neck = c.create_line(200, 150, 200, 130)
hat = c.create_polygon(180, 75, 220, 75, 200, 20, fill='blue')
words = c.create_text(200, 280, text="I am beauty from outta space!")


def blink(event):
    c.itemconfig(eye, fill='green')
    c.itemconfig(eyeball, state=HIDDEN)


def unblink(event):
    c.itemconfig(eye, fill='white')
    c.itemconfig(eyeball, state=NORMAL)


def burp(event):
    mouth_open()
    c.itemconfig(words, text="Buah!")


def steel_hat():
    c.itemconfig(hat, state=HIDDEN)
    c.itemconfig(words, text="Give me hat back!")


def mouth_open():
    c.itemconfig(mouth, fill='black')


def mouth_close():
    c.itemconfig(mouth, fill='red')


def eye_control(event):
    key = event.keysym
    if key == "Up":
        c.move(eyeball, 0, -1)
    elif key == "Down":
        c.move(eyeball, 0, 1)
    elif key == "Left":
        c.move(eyeball, -1, 0)
    elif key == "Right":
        c.move(eyeball, 1, 0)


c.bind_all('<KeyPress-a>', blink)
c.bind_all('<KeyPress-z>', unblink)
c.bind_all('<Button-1>', burp)
c.bind_all('<Key>', eye_control)

window.mainloop()
