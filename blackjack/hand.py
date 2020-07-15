"""
This module exports the 'Hand' class and related methods.
"""


class Hand:
    """
    A class defining the properties and methods of a hand object.

    A hand object is a collection of cards associated with either the dealer or the player. Within a round of blackjack,
    cards are added to a hand when the associated player chooses to 'hit'. The outcome of each round is determined by
    the relative values of the player's and dealer's hands.

    TODO: Define a __getitem__ and __len__ method to make the Hand class iterable
    """

    def __init__(self, holder_role):
        """
        Initialises an empty hand object for a given participant.

        Parameters
        ----------
        holder_role : str
            Defines the owner, or 'holder', of the hand object being created: either 'Player' or 'Dealer'
        """
        self._live_hand = []
        self._holder_role = holder_role

    def draw_card(self, deck_obj, face_dir):
        """
        Removes one card from the input deck and adds this card to the hand with orientation defined by 'face_dir'.

        Calls the 'deal_card' method of an input deck object, the deck returns a single card object and deletes this
        card from the deck. If the 'face_dir' input argument requires the hand to be dealt face-down, the freshly
        drawn card (face-up by default) calls its 'flip_card' method to ensure the card is correctly face-down before it
        it is appended to the hand array.

        TODO: Create a method 'hit' which just calls this method with card always face-up

        Parameters
        ----------
        deck_obj : blackjack.deck.Deck
            The game's 'live' deck object - a card will be removed from this deck and added to the current hand object
        face_dir : str
            Determines whether the card is added to the hand face-up or face-down; takes value 'up' or 'down'
        """
        drawn_card = deck_obj.deal_card()
        if face_dir == "down":
            drawn_card.flip_card()
        self._live_hand.append(drawn_card)

    def print_hand(self):
        """Prints the hand's owner followed by shorthand details of all cards currently within the hand."""
        print(f"\n{self._holder_role}'s hand")
        for idx, single_card in enumerate(self._live_hand):
            print(f"Card {idx}: {single_card.short_card_details()}")

    def hand_value(self):
        """
        Returns the total value of the target hand by summing the values of all constituent card objects.

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
