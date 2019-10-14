from tkinter import *
from pygame import mixer
import random
import time

# music and sounds
mixer.init()
mixer.music.load("files/runner.mp3")
mixer.music.set_volume(0.88)
mixer.music.play(-1)

# maintainance class
class Game:
	def __init__(self):
		self.tk = Tk()
		self.tk.title("Running Man")
		self.tk.resizable(0, 0)
		self.tk.wm_attributes("-topmost", 1)
		self.canvas = Canvas(self.tk, width=1400, height=900, highlightthickness=0)
		self.canvas.pack()
		self.canvas_height = 900
		self.canvas_width = 1400
		rand_bg = random.randint(1, 10)
		if rand_bg > 2: rand_bg = "1"
		else: rand_bg = "2"
		file_name = "img/background"+rand_bg+".gif"
		self.bg = PhotoImage(file=file_name)
		w = self.bg.width()
		h = self.bg.height()
		for x in range(14):
			for y in range(9):
				self.canvas.create_image(x*w, y*h, image=self.bg, anchor='nw')
		self.sprites = []
		self.running = True

	def mainloop(self):
		# game loop
		while True:
			if self.running:
				for sprite in self.sprites:
					sprite.move()
			self.tk.update_idletasks()
			self.tk.update()
			time.sleep(0.01)


# sprite coords
class Coords:
	def __init__(self, x1=0, y1=0, x2=0, y2=0):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2


# inheritor of game objects
class Sprite:
	def __init__(self, game):
		self.game = game
		self.endgame = False
		self.coordinates = None

	def move(self):
		pass

	def coords(self):
		return self.coordinates


# platforms objects class
class PlatformSprite(Sprite):
	def __init__(self, game, photo_image, x, y, width, height):
		Sprite.__init__(self, game)
		self.photo_image = photo_image
		self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor="nw")
		self.coordinates = Coords(x, y, x + width, y + height)


class MoovingPlatform(PlatformSprite):
	def __init__(self, game, photo_image, x, y, width, height):
		PlatformSprite.__init__(self, game, photo_image, x, y, width, height)
		self.speed = random.choice([1, 2, 3, -1, -2, -3])

	def move(self):
		x = self.coords().x1
		if x >= 1300 or x <= 0:
			self.speed *= -1
		self.game.canvas.move(self.image, self.speed, 0)

	def coords(self):
		# get self coordinates
		xy = self.game.canvas.coords(self.image)
		self.coordinates.x1 = xy[0]
		self.coordinates.y1 = xy[1]
		self.coordinates.x2 = xy[0] + 100
		self.coordinates.y2 = xy[1] + 10
		return self.coordinates


# running man
class StickFigureSprite(Sprite):
	def __init__(self, game):
		Sprite.__init__(self, game)
		# image
		self.images_left = self.get_images("L")
		self.images_right = self.get_images("R")
		self.image = game.canvas.create_image(200, 870, image=self.images_left[0], anchor="nw")
		# properties and coordinates
		self.x = -2
		self.y = 0
		self.current_image = 0
		self.current_image_add = 1
		self.jump_count = 0
		self.last_time = time.time()
		self.coordinates = Coords()
		# key listeners
		game.canvas.bind_all('<KeyPress-Left>', self.turn_left)
		game.canvas.bind_all('<KeyPress-Right>', self.turn_right)
		game.canvas.bind_all('<space>', self.jump)

	def turn_left(self, evt):
		# handler left
		if self.y == 0:
			self.x = -2

	def turn_right(self, evt):
		# handler right
		if self.y == 0:
			self.x = 2

	def jump(self, evt):
		# handler space
		if self.y == 0:
			self.y = -4
			self.jump_count = 0

	def animate(self):
		# man animation image count
		if self.x != 0 and self.y == 0:
			time_now = time.time()
			if time_now - self.last_time > 0.1:
				self.last_time = time_now
				self.current_image += self.current_image_add
				if self.current_image >= 2:
					self.current_image_add = -1
				if self.current_image <= 0:
					self.current_image_add = 1
		# image change
		if self.x < 0:
			if self.y != 0:
				self.game.canvas.itemconfig(self.image, image=self.images_left[2])
			else:
				self.game.canvas.itemconfig(self.image, image=self.images_left[self.current_image])
		elif self.x > 0:
			if self.y != 0:
				self.game.canvas.itemconfig(self.image, image=self.images_right[2])
			else:
				self.game.canvas.itemconfig(self.image, image=self.images_right[self.current_image])

	def coords(self):
		# get self coordinates
		xy = self.game.canvas.coords(self.image)
		self.coordinates.x1 = xy[0]
		self.coordinates.y1 = xy[1]
		self.coordinates.x2 = xy[0] + 27
		self.coordinates.y2 = xy[1] + 30
		return self.coordinates

	def move(self):
		self.animate()
		if self.y < 0:
			self.jump_count += 1
			if self.jump_count > 40:
				self.y = 4
		if self.y > 0:
			self.jump_count -= 1
		# collision flags
		co = self.coords()
		left = True
		right = True
		top = True
		bottom = True
		falling = True
		# collision with borders
		if self.y > 0 and co.y2 >= self.game.canvas_height:
			self.y = 0
			bottom = False
		elif self.y < 0 and co.y1 <= 0:
			self.y = 0
			top = False
		if self.x > 0 and co.x2 >= self.game.canvas_width:
			self.x = 0
			right = False
		elif self.x < 0 and co.x1 <= 0:
			self.x = 0
			left = False
		# collision with sprites
		for sprite in self.game.sprites:
			if sprite == self:
				continue
			sprite_co = sprite.coords()
			if top and self.y < 0 and collided_top(co, sprite_co):
				self.y = -self.y
				top = False
			if bottom and self.y > 0 and collided_bottom(self.y, co, sprite_co):
				self.y = sprite_co.y1 - co.y2
				if self.y < 0:
					self.y = 0
				bottom = False
				top = False
			if bottom and falling and self.y == 0 \
					and co.y2 < self.game.canvas_height \
					and collided_bottom(1, co, sprite_co):
				falling = False
			if left and self.x < 0 and collided_left(co, sprite_co):
				self.x = 0
				left = False
				if sprite.endgame:
					self.game.running = False
			if right and self.x > 0 and collided_right(co, sprite_co):
				self.x = 0
				right = False
				if sprite.endgame:
					self.game.running = False
		if falling and bottom and self.y == 0 and co.y2 < self.game.canvas_height:
			self.y = 4
		self.game.canvas.move(self.image, self.x, self.y)

	def get_images(self, flag):
		# returns move images lists
		images = []
		for i in range(1, 4):
			file_name = "img/figure-" + flag + str(i) + ".gif"
			images.append(PhotoImage(file=file_name))
		return images


# door sprite
class DoorSprite(Sprite):
	def __init__(self, game, photo_image, x, y, width, height):
		Sprite.__init__(self, game)
		self.photo_image = photo_image
		self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor="nw")
		self.coordinates = Coords(x, y, x + (width/2), y + height)
		self.endgame = True


# collision horizontal
def within_x(co1, co2):
	return (co1.x1 > co2.x1 and co1.x1 < co2.x2) \
			or (co1.x2 > co2.x1 and co1.x2 < co2.x2) \
			or (co2.x1 > co1.x1 and co2.x1 < co1.x2) \
			or (co2.x2 > co1.x1 and co2.x2 < co1.x2)

# collision vertical
def within_y(co1, co2):
	return (co1.y1 > co2.y1 and co1.y1 < co2.y2) \
			or (co1.y2 > co2.y1 and co1.y2 < co2.y2) \
			or (co2.y1 > co1.y1 and co2.y1 < co1.y2) \
			or (co2.y2 > co1.y1 and co2.y2 < co1.y2)

# collision check left
def collided_left(co1, co2):
	return within_y(co1, co2) and (co1.x1 <= co2.x2 and co1.x1 >= co2.x1)

# collision check right
def collided_right(co1, co2):
	return within_y(co1, co2) and (co1.x2 >= co2.x1 and co1.x2 <= co2.x2)

# collision check top
def collided_top(co1, co2):
	return within_x(co1, co2) and (co1.y1 <= co2.y2 and co1.y1 >= co2.y1)

# collision check bottom
def collided_bottom(y, co1, co2):
	y_calc = co1.y2 + y
	return within_x(co1, co2) and (y_calc >= co2.y1 and y_calc <= co2.y2)

# creates platforms
def create_platforms(game):
	for i in range(5):
		for j in range(1,4):
			create_one_platform(game, j, random.randint(0, 1300), 140 + i * 160)
	create_one_platform(game, 1, 20, 65)

	for i in range(10):
		create_one_platform(game, 1, random.randint(0, 1300), 100 + i * 80, True)


# creates one platform
def create_one_platform(game, size, x, y, moving=False):
	width = 32
	if size == 2: width = 66
	elif size == 1: width = 100
	file_name = "img/platform" + str(size) + ".gif"

	if moving:
		platform = MoovingPlatform(game, PhotoImage(file=file_name), x, y, width, 10)
	else:
		platform = PlatformSprite(game, PhotoImage(file=file_name), x, y, width, 10)
	game.sprites.append(platform)


game = Game()

# platforms and door
create_platforms(game)
door = DoorSprite(game, PhotoImage(file="img/door1.gif"), 45, 30, 40, 35)
game.sprites.append(door)

# running man
man = StickFigureSprite(game)
game.sprites.append(man)

game.mainloop()
