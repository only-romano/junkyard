import turtle

t = turtle.Pen()
t.penup()
turtle.bgcolor("black")

# check sides, min = 2, max = 6
sides = 4
try:
    sides = int(input("How many sides do you want? (2-6)\n"))
except Exception:
    sides = 4

if sides > 6:
    sides = 6
elif sides < 2:
    sides = 2

colors = ["red", "yellow", "blue", "orange", "green", "purple"]

for x in range(100):
    t.forward(x * 4)
    position = t.position()  # remember corner
    heading = t.heading()  # remember direction
    # little spiral inside every corner of big spiral
    for n in range(int(x/2)):
        t.pendown()
        t.pencolor(colors[n%sides])
        t.forward(2*n)
        t.right(360/sides - 2)
        t.penup()
    # Get back to remembered pos and direction
    t.setx(position[0])
    t.sety(position[1])
    t.setheading(heading)
    t.left(360/sides + 2)
