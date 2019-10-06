# Crazy eight game cards initialisation (deck and hand creation)
from random import choice
from card import Card


def init_cards():
    deck = create_deck()

    p_hand, deck = deal_cards(deck)
    c_hand, deck = deal_cards(deck)

    if choice([True, False]):
        p_hand, c_hand = c_hand, p_hand

    up_card = choice(deck)
    deck.remove(up_card)
    active_suit = up_card.suit
    return (deck, p_hand, c_hand, up_card, active_suit)


def create_deck():
    deck = []
    for suit in range(1, 5):
        for rank in range(1, 14):
            new_card = Card(suit, rank)
            if new_card.rank == 8:
                new_card.value = 50
            deck.append(new_card)
    return deck


def deal_cards(deck):
    hand = []
    for i in range(0, 5):
        card = choice(deck)
        hand.append(card)
        deck.remove(card)
    return (hand, deck)
