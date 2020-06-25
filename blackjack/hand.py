"""This module contains the 'Hand' class and related methods.
"""


class Hand:
    """ A class defining the properties and methods of a hand object. *** Add method overview ***
    """

    def __init__(self, holder_role):
        """ On initialisation, a hand object is created with an empty array to hold store card objects associated with
        the hand. The '_holder_role' stores the so-called hand type: e.g. player or dealer, which is required as an input
        argument when creating a hand object.
        """
        self._live_hand = []
        self._holder_role = holder_role

    def draw_card(self, deck_obj, face_dir):
        """ Calls the 'deal_card' method of an input deck object, deck returns single card object and deletes this card
        from the deck. If the 'face_dir' input argument requires the hand to be dealt face-down, the freshly
        drawn card (face-up by default) calls its 'flip_card' method to ensure the card is correctly face-down before it
        it is appended to the hand array.
        """
        drawn_card = deck_obj.deal_card()
        if face_dir == "down":
            drawn_card.flip_card()
        self._live_hand.append(drawn_card)

    def print_hand(self):
        """ Prints hand type followed by shorthand notation of all cards currently within the hand
        """
        print(f"\n{self._holder_role}'s hand")
        for idx, single_card in enumerate(self._live_hand):
            print(f"Card {idx}: {single_card.short_card_details()}")

    def hand_value(self):
        """ Returns the current numerical value of the target hand object.
        TODO: Between here and the 'card_value' method on card objects: need to account for situation where hand
        TODO: value is unknown because one or more cards are face-down AND the case where you have one/more aces within
        TODO: the hand and hence the hand can have two/more possible values.
        """
        indv_card_vals = []
        poss_hand_vals = []
        for card in self._live_hand:
            indv_card_vals.append(card.card_value())
        for i in range(len(indv_card_vals)):
            if isinstance(indv_card_vals[i], tuple):
                # some code that processes the two values of a tuple
                None
            elif isinstance(indv_card_vals[i], str):
                # some code that processes a value where the card was face-down and so returns the string: '*-*'
                None
