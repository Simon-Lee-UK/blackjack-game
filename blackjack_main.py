""" This module will define the flow of actions required to play a game of blackjack.
It has been separated out as its own file/module for readability.  Should make it easier to understand which sections of
code are executed for each action required in a game of blackjack.  This is a docstring, it's good practice to have one
at the start of each module (like here) and also as the first line of classes, functions and methods.  The goal is to
describe the block of code below, they'll be super helpful for us as we collaborate and start to get going.
"""
import pandas as pd
import numpy as np
from deck import Deck


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


if __name__ == '__main__':
    main()
