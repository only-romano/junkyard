# Computer turn
from random import choice

def ai_turn(deck, c_hand, up_card, active_suit, blocked):
    # can't make globals work
    options = []  # for ai to pick a best desision

    for card in c_hand:
        if card.rank == '8':
            # if ai got a 8, it plays it right away
            c_hand.remove(card)
            up_card = card
            print("Computer plays with", card)

            # finding best suit to pick
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
            return (deck, c_hand, up_card, active_suit, blocked)  # updated values

        else:
            # else finding available options for move
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
        print("Computer plays with", best_play)
    else:
        # ai has no options to play with, so
        if len(deck) > 0:
            # it takes a card
            next_card = choice(deck)
            c_hand.append(next_card)
            deck.remove(next_card)
            print("Computer takes a card.")
        else:
            # or can't take a card cause deck is empty
            print("Computer has no options and its pass.")
            blocked += 1

    print("Computer got %i cards" % (len(c_hand)))
    return (deck, c_hand, up_card, active_suit, blocked)  # updated values
