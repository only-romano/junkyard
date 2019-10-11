import turtle
from time import sleep


def filled_circle(r, g, b, rad=50):
    t.color(r, g, b)
    t.begin_fill()
    t.circle(rad)
    t.end_fill()


def my_square(size):
    for x in range(4):
        t.forward(size)
        t.left(90)


def my_star(size):
    for x in range(1, 19):
        t.forward(size)
        if x % 2 == 0:
            t.left(175)
        else:
            t.left(225)


def filled(func, args):
    t.begin_fill()
    func(args)
    t.end_fill()


t = turtle.Pen()

filled_circle(1, 1, 0)
filled_circle(0, 1, 0)
filled_circle(0, 0.5, 0)
filled_circle(1, 0, 0)
filled_circle(0.5, 0, 0)
filled_circle(0, 0, 1)
filled_circle(0, 0, 0.5)
filled_circle(0.9, 0.75, 0)
filled_circle(1, 0.7, 0.75)
filled_circle(1, 0.5, 0)
filled_circle(0.9, 0.5, 0.15)
filled_circle(0, 0, 0)
filled_circle(1, 1, 1)
t.reset()

my_square(50)
t.reset()
my_square(25)
my_square(50)
my_square(75)
my_square(100)
my_square(125)

t.reset()
filled(my_square, 50)
my_square(150)

t.reset()
t.color(0.9, 0.75, 0)
filled(my_star, 120)
t.color(0, 0, 0)
my_star(120)


sleep(1)
