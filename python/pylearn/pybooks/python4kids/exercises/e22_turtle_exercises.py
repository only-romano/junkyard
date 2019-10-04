import turtle
from time import sleep


def draw_star(size, points):
    for x in range(points):
        t.forward(size)
        t.left(150)


def filled(func, args):
    t.begin_fill()
    func(args)
    t.end_fill()


def polygon(args):
    sides = args[0]
    size = args[1]
    angle = 180 - (sides - 2) * 180 / sides
    for i in range(sides):
        t.forward(size)
        t.left(angle)


t = turtle.Pen()

t.color(1, 1, 0)
filled(polygon, [8, 100])
t.color(0, 0, 0)
polygon([8, 100])

draw_star(100, 12)

sleep(1)
