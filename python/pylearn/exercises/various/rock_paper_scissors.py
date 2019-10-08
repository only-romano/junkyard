import random

choices = ["rock", "paper", "scissors"]
print("Rules: rock beats scissors, paper flow rock, scissors cuts paper")
player = input("Choose rock, paper or scissors: ")
score_p = 0
score_c = 0

while not player.lower().startswith("q"):  # play while not quit input
    player = player.lower()
    computer = random.choice(choices)  # random choice comp
    if player.startswith("r"):
        player = "rock"
    elif player.startswith("p"):
        player = "paper"
    elif player.startswith("s"):
        player = "scissors"
    print("Your move -", player, "\nComputer's move -", computer)

    if player == computer:
        print("It's a draw!")
    elif player == "rock":
        if computer == "scissors":
            print("You won!")
            score_p += 1
        else:
            print("Computer won.")
            score_c += 1
    elif player == "paper":
        if computer == "rock":
            print("You won!")
            score_p += 1
        else:
            print("Computer won.")
            score_c += 1
    elif player == "scissors":
        if computer == "paper":
            print("You won!")
            score_p += 1
        else:
            print("Computer won.")
            score_c += 1
    else:
        print("There is an error in your input..")
    print("\nScore is: you - %i; computer - %i." % (score_p, score_c))
    player = input("Choose rock, paper or scissors to continue, or quit to exit: ")
