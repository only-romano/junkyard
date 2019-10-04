from turtle import *
from time import sleep

for i in range(3):
    forward(100)
    right(120)


def turtle_controller(do, val):
    do = do.upper()
    if do == "F":
        forward(val)
    elif do == "B":
        backward(val)
    elif do == "R":
        right(val)
    elif do == "L":
        left(val)
    elif do == "U":
        penup()
    elif do == "D":
        pendown()
    elif do == "N":
        reset()
    else:
        print("Unknown command")


def string_artist(string):
    cmd_list = string.split("-")
    for command in cmd_list:
        command = command.strip()
        length = len(command)
        if length:
            cmd_type = command[0]
            num = 0
            if length > 1:
                try:
                    num = int(command[1:])
                except Exception:
                    num = 0
            turtle_controller(cmd_type, num)


instructions = '''Input command for turtle:

Split commands with dash(-).
Example - F100-R45-U-F100-L45-D-F100-R90-B50

Commands:
N = New painting
U = Pen up (does not drawing if moving)
D = Pen down (drawing if moving)
	in next few commands you can use any over integers value, these given for example
F100 = forward by 100 units
B50 = backward by 50 units
R90 = right turn by 90 degrees
L45 = left turn by 45 degrees

END = Exit programm
'''

screen = getscreen()

while True:
    t_program = screen.textinput('Painting Automata', instructions)
    print(t_program)
    if t_program == None or t_program.upper() == 'END':
        break
    string_artist(t_program)

sleep(1)
