# Crazy Eights card game
import random
from cards import init_cards
from player import player_turn
from ai import ai_turn
from game_func import start_cards


p_score = c_score = 0  # total score
done = False           # final exit condition

while not done:
    deck, p_hand, c_hand, up_card, active_suit = init_cards()  # create lists of objects
    start_cards(p_hand)  # review start hand
    blocked = 0          # times pass

    game_done = False    # local game exit condition
    while not game_done:
        deck, p_hand, up_card, active_suit, blocked = player_turn(deck, p_hand, up_card, # turn +
                                                           active_suit, blocked)  # update values
        if len(p_hand) == 0:
            # player out of cards - WINNER
            game_done = True
            print("\nYou won!")

            # player score update
            p_points = 0
            for card in c_hand:
                p_points += card.value
            p_score += p_points
            print("You've got %i points!" % p_points)

        if not game_done:
            deck, c_hand, up_card, active_suit, blocked = ai_turn(deck, c_hand, up_card, # ai turn +
                                                              active_suit, blocked)  # update values
            if len(c_hand) == 0:
                # Computer out of cards. LOSE the game
                game_done = True
                print("\nComputer won.")

                # computer score update
                c_points = 0
                for card in p_hand:
                    c_points += card.value
                c_score += c_points
                print("Computer got %i points." % c_points)

            if blocked >= 2:
                # passes are run out, game over
                game_done = True
                print("There is no more passes. Game over.")

                # score update
                p_points = 0
                for card in c_hand:
                    p_points += card.value
                p_score += p_points
                c_points = 0
                for card in p_hand:
                    c_points += card.value
                c_score += c_points
                print("You scored %i points!" % p_points)
                print("Computer got %i points" % c_points)

        if game_done:
            # final exit condition check
            play_again = input("Do you want to play again? (y)\n")
            if play_again.lower().startswith('y'):
                done = False
                print("Your current total score is %i points!" % p_score)
                print("Computer current total score is %i points" % c_score)
            else:
                done = True
                print("Final score is:")
                print("You:  %i\tComputer: %i" % (p_score, c_score))
