""" This module will define the flow of actions required to play a game of blackjack.
It has been separated out as its own file/module for readability.  Should make it easier to understand which sections of
code are executed for each action required in a game of blackjack.  This is a docstring, it's good practice to have one
at the start of each module (like here) and also as the first line of classes, functions and methods.  The goal is to
describe the block of code below, they'll be super helpful for us as we collaborate and start to get going.
"""
import pandas as pd
import numpy as np
from deck import Deck
from hand import Hand


def main():
    """ Thinking about containing the game within a couple of while loops. The outer loop would just keep the game going
    until some exit command is received. The inner loop could be a while loop based on the length of the deck array.
    When the number of cards (length of array) dropped below a certain threshold value, that round would continue but
    then the loop is escaped and a totally new game deck is created to continue the game. You then re-enter this loop
    until another new deck is required.

    Current idea for hands is to have a small list of objects that is appended when dealt to and cleared out when the
    hand is discarded. Makes sense for deck objects to have a 'deal' method. How will this correctly pass cards to a
    hand?
    """
    first_deck = Deck()
    first_deck.print_deck()  # This prints details of the cards in the deck - currently nice to check it's working OK
    single_round(first_deck)  # This starts the first round of the game, providing the above deck object as input arg


def single_round(current_deck):
    """ Currently, not a full round. Just deals two cards to the player and two cards to the dealer then prints both
    hands. As these hands are defined within the 'single_round' function (and are not returned at the end), they only
    exist for a single round. For now, think this is fine. When writing info to StatJack, will need to ensure hand info
    is written from this function.
    """
    face_direction = ['up', 'down']  # Array storing two possible hand orientations: face-up and face-down
    players_hand = Hand('Player')  # Initialises a hand object for the player
    dealers_hand = Hand('Dealer')  # Initialises a hand object for the computer-controlled dealer
    for direction in face_direction:
        players_hand.draw_card(current_deck, 'up')
        dealers_hand.draw_card(current_deck, direction)  # Loop ensures dealer's first card is face-up, second face-down
    dealers_hand.print_hand()  # Prints the dealer's hand
    players_hand.print_hand()  # Prints the player's hand


if __name__ == '__main__':
    main()
