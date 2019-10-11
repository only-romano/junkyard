import turtle, time

pen = turtle.Pen()
pen.up()

for i in range(4):
	pen.forward(50)
	pen.down()
	pen.forward(100)
	pen.up()
	pen.forward(50)
	pen.right(90)

time.sleep(1)
