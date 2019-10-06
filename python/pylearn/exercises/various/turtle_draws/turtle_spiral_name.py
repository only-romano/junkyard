# цветная спираль из имени пользователя
import turtle

t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]

# gui text input
name = turtle.textinput("Введи своё имя", "Как тебя зовут?")

for x in range(100):
    t.pencolor(colors[x%4])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(name, font=("Arial", int((x + 4) / 4), "bold"))
    t.left(92)
