"""This module contains the 'Card' class and related methods.
"""
import pandas as pd
import numpy as np


class Card:
    """ A class defining the properties of a card object.
    """
    def __init__(self, input_suit, input_rank, input_value, input_deck_num):
        self._suit = input_suit
        self._rank = input_rank
        self._value = input_value
        self._deck_num = input_deck_num + 1

    def print_all_details(self):
        if self._rank == 'Ace':
            print('{} of {} (Value = {} or {}, Deck# = {})'
                  .format(self._rank, self._suit, str(self._value[0]), str(self._value[1]), str(self._deck_num)))
        else:
            print('{} of {} (Value = {}, Deck# = {})'
                  .format(self._rank, self._suit, str(self._value), str(self._deck_num)))
