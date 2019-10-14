from tkinter import *
from random import randint
from time import sleep, time
from math import sqrt

HEIGHT = 600
WIDTH = 800

TIME_LIMIT = 30
BONUS_SCORE = 1000

window = Tk()
window.title('Bubbles Hunter')

# Canvas
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='darkblue')
c.pack()

# Submarine
ship_id = c.create_polygon(5, 5, 5, 25, 30, 15, fill='red')
ship_id2 = c.create_oval(0, 0, 30, 30, outline='red')
SHIP_R = 15  # Radius of boat
SHIP_SPD = 10  # Speed of boat

# Move submarine to the center of screen
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
c.move(ship_id, MID_X, MID_Y)
c.move(ship_id2, MID_X, MID_Y)

# Bubbles
bub_id = list()  # list of bubbles names
bub_r = list()  # list of bubbles radiuses
bub_speed = list()  # list of bublles speed
MIN_BUB_R = 10  # minimal bubble radius
MAX_BUB_R = 30  # maximum bubble radius
MAX_BUB_SPD = 10  # maximum speed of bublle
GAP = 100
BUB_CHANCE = 10

# Score and time displays
c.create_text(50, 30, text='ВРЕМЯ', fill='white')
c.create_text(150, 30, text='СЧЁТ', fill='white')
time_text = c.create_text(50, 50, fill='white')
score_text = c.create_text(150, 50, fill='white')

# Score
score = 0
bonus = 0


# Functions block
def create_bubble():
    x = WIDTH + GAP
    y = randint(0, HEIGHT)
    r = randint(MIN_BUB_R, MAX_BUB_R)
    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline='white')
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(randint(1, MAX_BUB_SPD))


def move_bubbles():
    for i in range(len(bub_id)):
        c.move(bub_id[i], -bub_speed[i], 0)


def del_bubble(i):
    del bub_r[i]
    del bub_speed[i]
    c.delete(bub_id[i])
    del bub_id[i]


def get_coords(id_num):
    pos = c.coords(id_num)
    x = (pos[0] + pos[2]) / 2
    y = (pos[1] + pos[3]) / 2
    return x, y


def clean_up_bubs():
    for i in range(len(bub_id)-1, -1, -1):
        x, y = get_coords(bub_id[i])
        if x < -GAP:
            del_bubble(i)


def distance(id1, id2):
    x1, y1 = get_coords(id1)
    x2, y2 = get_coords(id2)
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


def collision():
    points = 0
    for bub in range(len(bub_id)-1, -1, -1):
        if distance(ship_id2, bub_id[bub]) < (SHIP_R + bub_r[bub]):
            points += (bub_r[bub] + bub_speed[bub])
            del_bubble(bub)
    return points


def show_score(score):
    c.itemconfig(score_text, text=str(score))


def show_time(time_left):
    c.itemconfig(time_text, text=str(time_left))


def move_parts(h, v):
    c.move(ship_id, h, v)
    c.move(ship_id2, h, v)


def move_ship(event):
    key = event.keysym
    if key == 'Up':
        move_parts(0, -SHIP_SPD)
    elif key == 'Down':
        move_parts(0, SHIP_SPD)
    elif key == 'Left':
        move_parts(-SHIP_SPD, 0)
    elif key == 'Right':
        move_parts(SHIP_SPD, 0)


def end_game():
    c.create_text(MID_X, MID_Y, text='GAME OVER', fill='white', font=('Helvetiva',30))
    c.create_text(MID_X, MID_Y + 30, text='Score: '+str(score), fill='white')
    c.create_text(MID_X, MID_Y + 45, text='Bonus time: '+str(bonus*TIME_LIMIT), fill='white')


# Event handlers
c.bind_all('<Key>', move_ship)

# Game time
end = time() + TIME_LIMIT
ended = False

# Main cycle
while time() < (end + 5):
    if ended:
        sleep(0.01)
        window.update()
        continue;
    if time() > end:
        end_game()
        ended = True
        window.update()
        continue
    if randint(1, BUB_CHANCE) == 1:
        create_bubble()
    move_bubbles()
    clean_up_bubs()
    score += collision()
    if (int(score / BONUS_SCORE)) > bonus:
        bonus += 1
        end += TIME_LIMIT
    show_score(score)
    show_time(int(end - time()))
    window.update()
    sleep(0.01)
