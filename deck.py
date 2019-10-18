"""This module contains the 'Deck' class and related methods.
"""
import pandas as pd
import numpy as np
from card import Card
from random import shuffle


class Deck:
    """ A class defining the properties and methods of a deck object. *** Add method overview ***
    """
    def __init__(self):
        """ For now, creating a Deck object initialises that object with four arrays:
        '_deck_array', '_suit_array', '_rank_array' and '_value_array' (the leading underscore is a Python convention;
        it hints that the variable is for internal use within the object's methods, i.e. it shouldn't be called when
        interacting with a 'Deck' object elsewhere in the code). The '_deck_array' is the most important feature of the
        Deck class; it is empty when defined but the 'new_deck' method, called at the end of init, will populate this
        list with 'Card' objects. The final three (lets call them 'property') arrays contain details of a standard deck
        of cards. Individual elements of these arrays are passed to a Card object when it is initialised. The
        '_suit_array' holds the four suits found in a pack of cards. The '_rank_array' holds the 13 ranks in each suit
        and the '_value_array' holds their corresponding values in the game of blackjack.
        """
        self._deck_array = []
        self._suit_array = ['spades', 'hearts', 'clubs', 'diamonds']
        self._rank_array = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
                            'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        self._value_array = [(1, 11), 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # Maybe change the Ace tuple to a dict?
        self.new_deck()

    def new_deck(self):
        """ The 'new_deck' method loops through a 'Deck' object's property arrays to populate the '_deck_array' with
        Card objects: together forming six full 52-card decks. Another 'Deck' method: 'shuffle_deck' is then
        called to randomly order the 312 'Card' objects within the list, giving a shuffled deck to start the game.
        """
        self._deck_array.clear()  # This line clears any existing elements from the '_deck_array' list (only required
        # when calling the method against an existing 'Deck' object, e.g.: " some_deck_object.new_deck() " would
        # effectively clear-out the existing deck, replacing it with a fresh one
        for i in range(6):
            for suit in self._suit_array:
                j = 0
                for rank in self._rank_array:
                    self._deck_array.append(Card(suit, rank, self._value_array[j], i))
                    #  self._deck_array[-1].print_all_card_details()  # Uncomment to print initial un-shuffled deck
                    j += 1
        self.shuffle_deck()  # Calls the 'shuffle_deck' method against the current Deck object (is this Pythonic code?)

    def shuffle_deck(self):
        """ When called, applies a new random ordering to the Card objects contained within a Deck object. Uses a method
        called 'shuffle' which is part of the 'random' package imported at the top of this module.
        """
        return shuffle(self._deck_array)

    def print_deck(self):
        """ Prints details of all cards within the Deck object (top to bottom)
        """
        for card in self._deck_array:
            card.print_all_card_details()
