# Player turn function
from random import choice
from game_func import show_cards, get_new_suit

def player_turn(deck, p_hand, up_card, active_suit, blocked):
    valid_play = False
    is_eight = False
    show_cards(p_hand, up_card, active_suit)

    selected_card = None
    response = input("Your turn.\nChoose card or \'Draw\' to pick up card: ")
    while not valid_play:
        while selected_card == None:
            if response.lower() == 'draw':
                valid_play = True
                if len(deck) > 0:
                    card = choice(deck)
                    p_hand.append(card)
                    deck.remove(card)
                    print("You took", card.long_name)
                else:
                    print("Deck has no more cards!")
                    blocked += 1
                return (deck, p_hand, up_card, active_suit, blocked)
            else:
                for card in p_hand:
                    if response.upper() == card.short_name:
                        selected_card = card
                if not selected_card:
                    response = input("You don't have that card! Please repeate! To pick a card input \'Draw\': ")

        if selected_card.rank == '8':
            valid_play = True
            is_eight = True
        elif selected_card.suit == active_suit or selected_card.rank == up_card.rank:
            valid_play = True

        if not valid_play:
            response = input("This is not accaptable play. Please repeat.")

    p_hand.remove(selected_card)
    up_card = selected_card
    print("You played with " + selected_card.long_name)
    if is_eight:
        active_suit = get_new_suit()
    else:
        active_suit = up_card.suit
    return (deck, p_hand, up_card, active_suit, blocked)
