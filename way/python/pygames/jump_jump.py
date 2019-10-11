from tkinter import *
import random
import time


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.started = False
        self.score = 0
        self.canvas.bind_all('<Button-1>', self.start_game)

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        elif self.hit_paddle(pos):
            y = -3
            if (self.paddle.x < 0 and self.x < 0) or (self.paddle.x > 0 and self.x > 0):
                y = -4
            self.y = y
            self.score += 1
            update_score(score_text, self.score)
        elif pos[3] >= self.canvas_height:
            global lives
            lives = lives - 1
            self.hit_bottom = True
            if lives == 0:
                end_game(end_text)
            else:
                time.sleep(2)
                self.canvas.move(self.id, 0, -370)
                self.hit_bottom = False
        if pos[0] <= 0:
            self.x = 3
        elif pos[2] >= self.canvas_width:
            self.x = -3

    def start_game(self, evt):
        self.started = True


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 350)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2


def end_game(text_id):
    time.sleep(0.3)
    canvas.itemconfig(text_id, state=NORMAL)


def update_score(score_id, score):
    canvas.itemconfig(score_id, text="Счёт: " + str(score))


window = Tk()
window.title("Прыг-Скок!")
window.resizable(0, 0)
window.wm_attributes("-topmost", 1)

canvas = Canvas(window, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
end_text = canvas.create_text(250, 200, text="Конец игры!", font=("Helvetica", 25), fill="red")
canvas.itemconfig(end_text, state=HIDDEN)
score_text = canvas.create_text(40, 15, text="Счёт: 0", font=("Helvetica", 15))

window.update()

lives = 3
paddle = Paddle(canvas, "blue")
ball = Ball(canvas, paddle, "red")


while True:
    if not ball.hit_bottom and ball.started:
        ball.draw()
        paddle.draw()
    window.update_idletasks()
    window.update()
    time.sleep(0.01)
