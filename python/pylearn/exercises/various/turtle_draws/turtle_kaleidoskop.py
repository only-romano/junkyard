import random, turtle

t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")

colors = ["red", "yellow", "blue", "orange", "green", "purple", "white", "gray"]


def spiral(x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()
    t.width(thick)
    for i in range(size):
        t.forward(i*2)
        t.left(360/sides +1)


for i in range(50):
    # random spiral in random place
    sides = random.randint(2, 7)
    thick = random.randint(1, 6)
    t.pencolor(random.choice(colors))
    size = random.randint(10, 40)
    x = random.randrange(0, turtle.window_width()//2)
    y = random.randrange(0, turtle.window_height()//2)
    # spirals
    spiral(x, y)
    spiral(-x, y)
    spiral(-x, -y)
    spiral(x, -y)
