# Guess the number!
import easygui
from random import randint
SAVEFILE_PATH = "data/save.txt"

def load_savefile():
    saves = {}
    with open(SAVEFILE_PATH) as savefile:
        for line in savefile:
            if len(line):
                save = line.split(',')
                name = save[0]
                score = int(save[1])
                saves[name] = score
    return saves


def update_savefile(saves, name, score):
    saves[name] = score
    return saves


def write_savefile(saves):
    with open(SAVEFILE_PATH, "w") as savefile:
        for key in saves:
            savefile.write(key + "," + str(saves[key]) + ",\n")


SAVES = load_savefile()

easygui.msgbox("Hello, this is \"Guess the Number!\" game, please introduce yourself!")
name = easygui.enterbox("What is your name?")
score = 100
easygui.msgbox("It's nice to meet you, " + name + "!")

flag_name = False
for key in SAVES:
    if key == name:
        score = SAVES[name]
        flag_name = True

if flag_name:
    reset = easygui.enterbox("Glad to see you again! I miss ya! Can I tell you, what y" +
    	"ou've got " + str(score) + " credits on your's account?\nIf you want to cance" +
    	"l all progress and get default credits please input \"reset\" (without braces).")
    if reset.lower() == "reset":
        score = 100
        easygui.msgbox("Done! Now you've got 100 credits again! Best casino in the world.")
else:
    easygui.msgbox("Welcome to our math casino. We glad to present you 100 free credits!")

easygui.msgbox("\n\tRules:\n\nEvery round you make a bet, what number it will be - 1, 2" +
	" or 3, if your guess is correct - your bet is doubled, if not - sorry, but you los" +
	"t your bet.\nShall we get started?\n\n")

words = [
    "Bul bul bul bul bul! It's ready!",
    "Shalom, comrades, number has taken it's place!",
    "Boom, it's my heartbeating around number!",
    "So, guess the number has been choosen!",
    "Coocoo is anyone here? It's me! You're lucky number!",
    "Here we go!"
]

init_score = score

while True:
    if score == 0:
        break
    easygui.msgbox(name + ", your account is - " + str(score) + " credits")
    odd = 0
    try:
        odd = easygui.integerbox("Make your bet amount! - ")
    except Exception:
        odd = 1
    if odd >= score:
        easygui.msgbox("It's all in!")
        odd = score
    score = score - odd
    easygui.msgbox("\nThank you, bets are placed! Ball is running for number " + str(randint(1, 3)) +
    	" or... not!? Spin round, wanna make for you grand, " + name + "!")
    ball = randint(1, 3)
    easygui.msgbox(words[randint(0, 5)])
    answer = easygui.integerbox("So! What is your guess, " + name + ", (1, 2 or 3) - ?")
    try:
        answer = int(answer)
    except Exception:
        answer = 0
        easygui.msgbox("Well, you gotta take it more seriously, it's 1, 2 or 3, but not your credit card number")
    if answer == ball:
        score = score + odd * 2
        easygui.msgbox("Hurray, hurray, hurray! You won! You double your bet! Now your account is - " + str(score) + " credits!")
    else:
        easygui.msgbox("Well... Bad luck.. Don't worry to much, it'll be more luck next time!")

    finish = easygui.enterbox("Shall we continue? (input any number or letter to continue) Leave empty to exit")
    if not len(finish):
        break

easygui.msgbox("Thank you for playing with us, " + name + "!")

if init_score > score:
    easygui.msgbox("You lose some money today, it's " + str((init_score - score)) + " credits.. Don't be sad!")
elif init_score < score:
    easygui.msgbox("Congrats! You won today " + str((score - init_score)) + " credits!")
else:
    easygui.msgbox("It's a draw. None lost, none won.")

easygui.msgbox("Your account - " + str(score) + " credits!")
easygui.msgbox("\nTo continue the game with your account don't forget your name! Letter Case is important!")
easygui.msgbox("Goodbye, " + name + "!")

SAVES = update_savefile(SAVES, name, score)
write_savefile(SAVES)
