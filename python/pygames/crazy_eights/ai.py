# Ai turn
from random import choice

def ai_turn(deck, c_hand, up_card, active_suit, blocked):
    options = []
    for card in c_hand:
        if card.rank == '8':
            c_hand.remove(card)
            up_card =card
            print("Computer plays wth " + card.long_name)
            suit_totals = [0, 0, 0, 0]
            for suit in range(1, 5):
                for card in c_hand:
                    if card.suit_id == suit:
                        suit_totals[suit-1] += 1
            long_suit = 0
            for i in range(4):
                if suit_totals[i] > long_suit:
                    long_suit = i
            if long_suit == 0: active_suit = "Diamonds"
            elif long_suit == 1: active_suit = "Hearts"
            elif long_suit == 2: active_suit = "Spades"
            elif long_suit == 3: active_suit = "Clubs"
            print("Computer changes suit with " + active_suit)
        else:
            if card.suit == active_suit or card.rank == up_card.rank:
                options.append(card)

    if len(options) > 0:
        best_play = options[0]
        for card in options:
            if card.value > best_play.value:
                best_play = card

        c_hand.remove(best_play)
        up_card = best_play
        active_suit = up_card.suit
        print("Computer plays with " + best_play.long_name)
    else:
        if len(deck) > 0:
            next_card = choice(deck)
            c_hand.append(next_card)
            deck.remove(next_card)
            print("Computer takes a card.")
        else:
            print("Computer has no options and its pass.")
            blocked += 1
    print("Computer got %i cards" % (len(c_hand)))
    return (deck, c_hand, up_card, active_suit, blocked)
