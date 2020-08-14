"""
This module exports the 'Hand' class, 'PlayerHand' and 'DealerHand' subclasses, and related methods.
"""


class Hand:
    """
    A class defining the properties and methods of a hand object.

    A hand object is a collection of cards associated with either the dealer or the player. Within a round of blackjack,
    cards are added to a hand when the associated player chooses to 'hit'. The outcome of each round is determined by
    the relative values of the player's and dealer's hands.
    """

    def __init__(self, holder_role="Player"):
        """
        Initialises an empty hand object for a given participant.

        Parameters
        ----------
        holder_role : str
            Defines the owner, or 'holder', of the hand object bseing created: either 'Player' or 'Dealer'.
            Defaults to 'Player' for this base hand class.
        """
        self._live_hand = (
            []
        )  # A list of card objects making up the hand; initialised as an empty list
        self._active = True  # The active status communicates whether the hand is still active in the current round
        self._bust = False  # The bust status communicates whether the hand is bust (value > 21) in the current round
        self._holder_role = holder_role

    def __iter__(self):
        """
        Allows hand objects to be iterated over, yielding constituent card objects in the order they were added.

        Yields
        ------
            card : blackjack.card.Card
                The next card in the hand (within the hand object's '_live_hand' attribute).
        """
        for card in self._live_hand:
            yield card

    def __repr__(self):
        """
        Entering the reference for a hand object in the terminal triggers this method, printing all hand details.

        Returns
        -------
            Output of 'print_hand' method : str
                Prints the hand's owner followed by shorthand details of all cards currently within the hand.
        """
        return self.print_hand()

    def __len__(self):
        """Allows len() to be used on hand objects, returning the number of cards in the hand as the object 'length'."""
        return len(self._live_hand)

    @property
    def hand_value(self):
        """
        Returns the total value(s) of the target hand by summing the values of all constituent card objects.

        Returns
        -------
        hand_value_list : list of int / str
            A list containing all possible values the hand's combination of cards can take with no duplicates. For a
            hand with all cards face-up: returns a list of integers. For hands with any cards face-down: returns a
            list of strings.
        """
        ace_count = 0
        ace_values = None
        face_down_count = 0
        non_ace_sum = 0

        # Loop: counts number of face-down cards in the hand; counts face-up aces; sums face-up cards that aren't an ace
        for card in self:
            # Try statement catches TypeErrors thrown when 'is_ace' method encounters a face-down card
            try:
                if card.is_ace():
                    ace_count += 1
                    ace_values = card.card_value()
                else:
                    non_ace_sum += card.card_value()
            except AssertionError:
                face_down_count += 1

        # This if-else block defines a list of possible values associated with all face-up cards in the hand
        if ace_count > 0:
            ace_sum_possibilities = self._calculate_ace_values(ace_count, ace_values)
            ace_sum = [
                possibility + non_ace_sum for possibility in ace_sum_possibilities
            ]
            hand_value_list = ace_sum
        else:
            hand_value_list = [non_ace_sum]

        # Where the hand contains face-down cards, this block adds the consistent face-down string to the face-up values
        if face_down_count > 0:
            hand_value_list = [
                str(value) + " + *-*" * face_down_count for value in hand_value_list
            ]

        return hand_value_list

    def is_active(self):
        """
        As a boolean, returns the active status of the hand in the current round (bust/stand = False; otherwise = True).

        A hand is regarded as active in a round while cards can still be added to the hand. Once a player decides to
        'stand' at their hand's current value, or if they go bust (> 21), the hands '_active' attribute is set to False
        signalling that no further actions are required by the player holding the hand in the current round.

        Returns
        -------
        bool
            True when hand can still receive cards in the current round; otherwise False.
        """
        return self._active

    def is_bust(self):
        """
        As a boolean, returns 'bust' status of hand in the current round (value > 21: returns True; otherwise False).

        Returns
        -------
        bool
            True when lowest possible hand value exceeds 21; otherwise False.
        """
        return self._bust

    def stand(self):
        """Updates hand status to inactive: triggered when player chooses to draw no more cards in the current round."""
        self._active = False

    def draw_card(self, deck_obj, face_dir="up"):
        """
        Removes one card from the input deck and adds this card to the hand with orientation defined by 'face_dir'.

        Calls the 'deal_card' method of an input deck object, the deck returns a single card object and deletes this
        card from the deck. If the 'face_dir' input argument requires the hand to be dealt face-down, the freshly
        drawn card (face-up by default) calls its 'flip_card' method to ensure the card is correctly face-down before it
        it is appended to the hand array.

        Parameters
        ----------
        deck_obj : blackjack.deck.Deck
            The game's 'live' deck object - a card will be removed from this deck and added to the current hand object.
        face_dir : str
            Defines whether card is added to the hand face-up or face-down. By default, the card will be added
            face-up with face_dir = 'up'. Any value of face_dir not spelling 'up' (case-insensitive) will add the card
            face-down.

        Raises
        ------
        AssertionError
            Raised when the hand is inactive (can't accept further cards).
        """
        assert self.is_active(), "Cannot draw a card to this hand: it is marked as inactive in the current round."
        drawn_card = deck_obj.deal_card()
        if face_dir.lower() != "up":
            drawn_card.flip_card()
        self._live_hand.append(drawn_card)

    def print_hand(self):
        """
        Prints the hand's owner followed by shorthand details of all cards currently within the hand.

        Returns
        -------
        empty_string : str
            An empty string, returned so that the 'print_hand' method can be called by the Hand class' __repr__
            method which must return a string-like object.
        """
        empty_string = ""
        print(f"\n{self._holder_role}'s hand")
        for idx, single_card in enumerate(self):
            print(f"Card {idx}: {single_card.short_card_details()}")
        print(f"Value: {self.hand_value}")
        return empty_string

    @staticmethod
    def _calculate_ace_values(ace_count, ace_values):
        """
        Returns the possible values of a collection of ace cards as a sorted list.

        Parameters
        ----------
        ace_count : int
            The number of ace cards to calculate possible summed values for.
        ace_values : tuple
            A two-element tuple containing the possible card values an ace can take e.g. (1, 11).

        Returns
        -------
        ace_sum_possibilities : list of int
            A list containing each value 'ace_count' number of aces can combine to make.

        TODO: Refactor to allow any number of possible ace values (additional loop over keys of dict?)
        """
        ace_sum_possibilities = [0]
        for ace_idx in range(ace_count):
            first_set = [
                ace_values[0] + ace_sum_element
                for ace_sum_element in ace_sum_possibilities
            ]
            second_set = [
                ace_values[1] + ace_sum_element
                for ace_sum_element in ace_sum_possibilities
            ]
            ace_sum_possibilities = list(set(first_set + second_set))
            ace_sum_possibilities.sort()
        return ace_sum_possibilities


class DealerHand(Hand):
    """
    A subclass defining the properties and methods specific to a hand object held by the dealer.

    The dealer's hand is unique because: the first card dealt to the dealer will always be dealt face-down;
    the dealer's turn in a single round must be resolved automatically.
    """

    def __init__(self):
        """Calls the __init__ method of the base Hand class, initialising an empty hand object for the dealer."""
        super().__init__("Dealer")

    def draw_card(self, deck_obj, face_dir=None):
        """
        Removes one card from the input deck and adds this card to the hand with orientation defined by 'face_dir'.

        Parameters
        ----------
        deck_obj : blackjack.deck.Deck
            The game's 'live' deck object - a card will be removed from this deck and added to the dealer's hand object.
        face_dir : None / str
            Defines whether card is added to the hand face-up or face-down. By default, 'face_dir' is None when
            method is called against a dealer's hand object. Where None, the orientation of the card is determined
            by the number of cards currently in the dealer's hand. If the dealer currently has a single card in their
            hand, the card is dealt face-down; otherwise face-up. If the method is called with face_dir specified, it
            behaves identically to the equivalent method on the base Hand class.
        """
        if face_dir:
            super().draw_card(deck_obj, face_dir)
        elif len(self) == 1:
            face_dir = "down"
            super().draw_card(deck_obj, face_dir)
        else:
            face_dir = "up"
            super().draw_card(deck_obj, face_dir)
