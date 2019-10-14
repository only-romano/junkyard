# Smile draw
import turtle, random

t = turtle.Pen()
t.speed(0)
t.hideturtle()
turtle.bgcolor("black")


def draw_smiley(x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()
    # head
    draw_smiley_head()
    # eyes
    draw_smiley_eye(x, y)
    draw_smiley_eye(x, y, False)
    # mounth
    draw_smiley_mouth(x, y)


# head
def draw_smiley_head():
    color = random.choice(["yellow", "purple", "white", "gray"])
    t.pencolor(color)
    t.fillcolor(color)
    draw_circle(50)

# eyes
def draw_smiley_eye(x, y, left=True):
    if left: x -= 15
    else: x += 15
    t.setpos(x, y+60)
    if left: t.fillcolor(random.choice(["blue", "green"]))
    draw_circle(10)

# mouth
def draw_smiley_mouth(x, y):
    t.setpos(x-25, y+40)
    t.pencolor(random.choice(["black", "red"]))
    t.width(10)
    t.goto(x-10, y+20)
    t.goto(x+10, y+20)
    t.goto(x+25, y+40)
    t.width(1)

# circle
def draw_circle(size):
    t.begin_fill()
    t.circle(size)
    t.end_fill()


for n in range(50):
    x = random.randrange(-turtle.window_width()//2, turtle.window_width()//2)
    y = random.randrange(-turtle.window_height()//2, turtle.window_height()//2)
    draw_smiley(x, y)
