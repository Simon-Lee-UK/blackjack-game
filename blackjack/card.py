"""
This module exports the 'Card' class and related methods.
"""


class Card:
    """
    A class defining the properties and methods of a card object.

    A single card object represents a single playing card. By default, cards are created face up, typically within
    methods of the deck class. The suit, rank and value of a card object are defined at initialisation and must remain
    constant for its lifetime. Card objects have methods to flip the card and print details of the card's suit, rank,
    etc.
    """

    def __init__(
        self, input_suit, input_rank, input_rank_short, input_value, input_deck_num
    ):
        """
        Initialises a card object with attributes set by the input arguments.

        Parameters
        ----------
        input_suit : str
            Defines the card's suit e.g. 'Clubs'
        input_rank : str
            Defines the card's rank e.g. 'Jack'
        input_rank_short : str
            A shortened variant of the card's rank e.g. 'J'
        input_value : int / tuple
            The value associated with the card's rank
            Aces can take one of two values - these are input as a tuple: (1, 11)
        input_deck_num : int
            Records which 52-card deck the card has been initialised for
            i.e. no deck should have cards with identical values for: 'input_suit', 'input_rank' and 'input_deck_num'
        """
        self._suit = input_suit
        self._rank = input_rank
        self._rank_short = input_rank_short
        self._value = input_value
        self._deck_num = (
            input_deck_num + 1
        )  # Accounts for zero-indexing: _deck_num will be an integer >= 1
        self._face_up = True  # This boolean stores whether the card is face up (True) or face down (False)

    def __repr__(self):
        """
        Entering the reference for a card object in the terminal triggers this method, printing all card details.

        Returns
        -------
            Output of 'print_card_details' method : str
                Prints verbose attributes of a Card object, e.g.: 'Ace of diamonds (Value = 1 or 11, Deck# = 3)'.
        """
        return self.print_card_details()

    def print_card_details(self):
        """
        Prints verbose attributes of a Card object, e.g.: 'Ace of diamonds (Value = 1 or 11, Deck# = 3)'.

        Returns
        -------
        empty_string : str
            An empty string, returned so that the 'print_card_details' method can be called by the Card class' __repr__
            method which must return a string-like object.

        TODO: Add face-down card privacy to this method? Currently only called by for cards in deck.
        """
        empty_string = ""
        if self._rank == "Ace":
            print(
                f"{self._rank} of {self._suit.lower()} "
                f"(Value = {str(self._value[0])} or "
                f"{str(self._value[1])}, "
                f"Deck# = {str(self._deck_num)})"
            )
        else:
            print(
                f"{self._rank} of "
                f"{self._suit.lower()} "
                f"(Value = {str(self._value)}, "
                f"Deck# = {str(self._deck_num)})"
            )
        return empty_string

    def flip_card(self):
        """'Flips' the card object by setting the '_face_up' attribute to the opposite boolean value."""
        self._face_up = not self._face_up

    def card_value(self):
        """
        If card is currently face-up, returns card value; if face-down returns a consistent string.

        Returns
        -------
        int / str
            If card is face-up: returns card value as integer; otherwise returns 'face-down string' = '*-*'.
        """
        if self._face_up:
            return self._value
        else:
            return "*-*"

    def is_ace(self):
        """
        Face-up cards: return True if card is an Ace and False if it isn't; face-down cards raise a TypeError.

        Returns
        -------
        bool
            True for face-up aces; false for face-up cards that are not an ace.

        Raises
        ------
        TypeError
            Raised when the card is face-down.
        """
        if self._rank == "Ace" and self.is_face_up():
            return True
        elif self._rank != "Ace" and self.is_face_up():
            return False
        else:
            raise TypeError("Cannot resolve 'is_ace': card is face down.")

    def is_face_up(self):
        """
        Returns the current card orientation as a boolean (face-up = True, face-down = False).

        Returns
        -------
        bool
            True when card is face-up; False when card is face-down.
        """
        return self._face_up

    def short_card_details(self):
        """
        If card is currently face-up, returns shorthand card details; if face-down returns a consistent string.

        Returns
        -------
        str
            If card is face-up: returns shorthand card details; otherwise returns 'face-down string' = '*-*'.
        """
        if self._face_up:
            return f"{self._rank_short}-{self._suit[0]}"
        else:
            return "*-*"
