# start_cards - shows starting hand with explanations of long name card

def start_cards(hand):
    print("Your hand is:")
    for card in hand:
        print(card.short_name, "=", card.long_name, "- Value:", card.value)


def show_cards(p_hand, up_card, active_suit):
    message = "Your hand is: "
    for card in p_hand:
        message += card.short_name + ", "
    message += "Opened card is " + up_card.short_name
    message += "\nSuit is " + active_suit
    print(message)


def get_new_suit(active_suit):
    got_suit = False
    while not got_suit:
        suit = input("Pick a suit: ")
        if suit.lower().startswith("d"):
            active_suit = "Diamonds"
            got_suit = True
        elif suit.lower().startswith("s"):
            active_suit = "Spades"
            got_suit = True
        elif suit.lower().startswith("h"):
            active_suit = "Hearts"
            got_suit = True
        elif suit.lower().startswith("c"):
            active_suit = "Clubs"
            got_suit = True
        else:
            print("Incorrect suit - please repeat.")
    print("You choose " + active_suit)
    return active_suit
