"""This module contains the 'Deck' class and related methods.
"""
import pandas as pd
import numpy as np


class Deck:
    """ A class defining the properties of a deck object.  For now, creating a Deck object just creates an array
    called '_suit_array'.  The leading underscore is a Python convention; it hints that the variable is for internal use
    within the object's methods, i.e. it shouldn't be called when interacting with a 'Deck' object elsewhere in the
    code. The '_suit_array' holds the four suits found in a pack of cards.
    """
    def __init__(self):
        self._suit_array = ['spades', 'hearts', 'clubs', 'diamonds']
        self._rank_array = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
                            'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        self._value_array = [(1, 11), 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # Maybe change the Ace tuple to a dict?
        print(self._suit_array)
        print(self._rank_array)
        print(self._value_array)

    def new_deck(self):
        for suit in self._suit_array:
            for rank in self._rank_array:
                print(rank + " of " + suit)
