import turtle

t = turtle.Pen()
t.reset()
t.color(1, 0, 0)


# Кузов
t.begin_fill()

t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)

t.end_fill()


# Переднее колесо
t.color(0, 0, 0)
t.up()
t.forward(10)
t.down()

t.begin_fill()
t.circle(10)
t.end_fill()


# Заднее колесо
t.setheading(0)
t.up()
t.forward(90)
t.right(90)
t.forward(10)
t.setheading(0)
t.down()

t.begin_fill()
t.circle(10)
t.end_fill()
