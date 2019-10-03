import turtle
from time import sleep

def turtle_print(t, end, to_for, to_left):
    t.reset()
    for x in range(1, end):
        t.forward(to_for)
        t.left(to_left)


t = turtle.Pen()

turtle_print(t, 5, 50, 90)  # квадрат
turtle_print(t, 9, 100, 225)  # звезда с 8 концами
turtle_print(t, 38, 100, 175)  # звезда с 37 концами
turtle_print(t, 20, 100, 95)  # спиралевидная звезда

# ещё одна звезда
t.reset()
for x in range(1, 19):
    t.forward(100)
    if x % 2 == 0:
        t.left(175)
    else:
        t.left(225)

sleep(1)
