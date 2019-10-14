from turtle import Pen
from time import sleep


class Things:
	pass


class Inanimate(Things):
	pass

class Animate(Things):
	pass


class Sidewalks(Inanimate):
	pass


class Animals(Animate):
	def breathe(self):
		print("дышит")
	def move(self):
		print("двигается")
	def eat_food(self):
		print("ест")


class Mammals(Animals):
	def feed_young_with_milk(self):
		print("кормит детёнышей молоком")


class Giraffes(Mammals):
	def __init__(self, spots):
		self.giraffe_spots = spots

	def eat_leaves_from_trees(self):
		print("ест листья")
		self.eat_food()

	def find_food(self):
		self.move()
		print("Я нашёл еду!")
		self.ear_food()

	def left_foot_forward(self):
		print("левая нога впереди")

	def right_foot_forward(self):
		print("правая нога впереди")

	def left_foot_back(self):
		print("левая нога сзади")

	def right_foot_back(self):
		print("правая нога сзади")

	def dance_a_jig(self):
		self.left_foot_forward()
		self.left_foot_back()
		self.right_foot_forward()
		self.right_foot_back()
		self.left_foot_back()
		self.right_foot_back()
		self.right_foot_forward()
		self.left_foot_forward()
		self.move()
		self.move()
		self.move()


reginald = Giraffes(100)
reginald.dance_a_jig()


t1 = Pen()
t2 = Pen()
t3 = Pen()
t4 = Pen()

t1.forward(100)
t1.left(90)
t2.forward(120)
t2.left(90)
t3.forward(120)
t3.right(90)
t4.forward(100)
t4.right(90)

t1.forward(70)
t1.right(90)
t2.forward(40)
t2.right(90)
t3.forward(40)
t3.left(90)
t4.forward(70)
t4.left(90)

t1.forward(70)
t2.forward(30)
t3.forward(30)
t4.forward(70)

sleep(2)
