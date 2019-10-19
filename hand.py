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

    def draw_card(self, deck_obj, face_dir):
        """ Call method of the deck, deck returns single card object and deletes this card from the deck.
        face_dir argument is checked against the face-up property of the card; if it differs, flip_card method is called
        Finally, once card is in correct orientation, it is appended to the hand array.
        """
        drawn_card = deck_obj.deal_card()
        if face_dir == 'down':
            drawn_card.flip_card()
        self._hand_array.append(drawn_card)
