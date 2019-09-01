"""This module contains the 'Deck' class and related methods.
"""


class Deck:
    """ A class defining the properties of a deck object.  For now, creating a Deck object just creates an empty array
    called '_suit_array'.  The leading underscore is a Python convention; it hints that the variable is for internal use
    within the object's methods, i.e. it shouldn't be called when interacting with a 'Deck' object elsewhere in the
    code.
    """
    def __init__(self):
        self._suit_array = []
