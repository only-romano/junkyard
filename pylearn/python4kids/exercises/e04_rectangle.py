import turtle, time

pen = turtle.Pen()

for i in range(4):
	if i % 2 != 0:
		pen.forward(100)
	else:
		pen.forward(200)
	pen.right(90)

time.sleep(1)
