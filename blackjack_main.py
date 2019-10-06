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
    first_deck = Deck()
    first_deck.new_deck()


if __name__ == '__main__':
    main()
