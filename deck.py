"""This module contains the 'Deck' class and related methods.
"""
import pandas as pd
import numpy as np


class Deck:
    """ A class defining the properties and methods of a deck object. *** Add method overview ***
    """
    def __init__(self):
        """ For now, creating a Deck object initialises that object with three arrays:
        '_suit_array', '_rank_array' and '_value_array' (the leading underscore is a Python convention; it hints that
        the variable is for internal use within the object's methods, i.e. it shouldn't be called when interacting with
        a 'Deck' object elsewhere in the code). The '_suit_array' holds the four suits found in a pack of cards.
        The '_rank_array' holds the 13 ranks in each suit and the '_value_array' holds their corresponding values in the
        game of blackjack.
        """
        self._suit_array = ['spades', 'hearts', 'clubs', 'diamonds']
        self._rank_array = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
                            'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        self._value_array = [(1, 11), 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # Maybe change the Ace tuple to a dict?
        # print(self._suit_array)
        # print(self._rank_array)
        # print(self._value_array)

    def new_deck(self):
        """ The 'new_deck' method loops through a 'Deck' object's arrays to a list of six 52-card decks. Currently, the
        method just prints the suit, rank and value of each individual card. The 'new_deck' method will be edited to
        instead create 'Card' objects according to these specifications. Another 'Deck' method: 'shuffle' will then be
        called to randomly order the 312 'Card' objects within the list, giving a shuffled deck to start the game.
        """
        for i in range(6):
            for suit in self._suit_array:
                j = 0
                for rank in self._rank_array:
                    if rank == 'Ace':
                        print('{} of {} (Value = {} or {}, Deck# = {})'
                              .format(rank, suit, str(self._value_array[j][0]), str(self._value_array[j][1]), str(i+1)))
                    else:
                        print('{} of {} (Value = {}, Deck# = {})'
                              .format(rank, suit, str(self._value_array[j]), str(i + 1)))
                    j += 1
