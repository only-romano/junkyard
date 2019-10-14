import turtle

t = turtle.Pen()
turtle.bgcolor("black")

sides = 6
try:
    sides = int(input("How many sides do you want?\n"))
except Exception:
    sides = 6

colors = ["red", "yellow", "blue", "orange", "green", "purple"]

for x in range(360):
    col_num = sides
    if sides > 6:
        col_num = 6
    t.pencolor(colors[x%col_num])
    t.forward(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x * sides/200)
