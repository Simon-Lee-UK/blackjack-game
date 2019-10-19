"""This module contains the 'Hand' class and related methods.
"""


class Hand:
    """ A class defining the properties and methods of a hand object. *** Add method overview ***
    """
    def __init__(self, hand_type):
        """ On initialisation, a hand object is created with an empty array to hold store card objects associated with
        the hand. The '_type_id' stores the so-called hand type e.g. player or dealer which is required as an input
        argument when creating a hand object."""
        self._hand_array = []
        self._type_id = hand_type
