# Ghost Game
from random import randint

print("Ghost house")

feeling_brave = True
score = 0

while feeling_brave:
    ghost_door = randint(1, 3)
    print("There are 3 doors upward...")
    print("And these a ghost behind one of them!")
    print("Which door you choosing?")
    door = input("1, 2 or 3?\n")
    
    try:
        door_num = int(door)
    except Exception:
        door_num = ghost_door
    
    if door_num < 1 or door_num > 3:
        door_num = ghost_door

    if door_num == ghost_door:
        print("Ghost!")
        feeling_brave = False
    else:
        print("There is no ghost!")
        print("You going to the next room.")
        score += 1

print("Run!")
print("Game over! You scored %s points!" % score)
