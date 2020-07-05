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
            description
        input_rank : str
            description
        input_rank_short : str
            description
        input_value : int / tuple
            description
        input_deck_num : int
            description
        """
        self._suit = input_suit
        self._rank = input_rank
        self._rank_short = input_rank_short
        self._value = input_value
        self._deck_num = input_deck_num + 1
        self._face_up = True  # This logical stores whether the card is face up (True) or face down (False)

    def print_card_details(self):
        """Prints verbose attributes of a Card object, e.g.: 'Ace of diamonds (Value = 1 or 11, Deck# = 3)'."""
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

    def flip_card(self):
        """'Flips' the card object by setting '_face_up' to the opposite boolean value."""
        self._face_up = not self._face_up

    def card_value(self):
        """Returns the value of the card. Value can be a tuple (for an Ace) or an integer value (all other cards)."""
        if self._face_up:
            return self._value
        else:
            return "*-*"

    def is_face_up(self):
        """Returns the current card orientation as a boolean (face-up = True, face-down = False)."""
        return self._face_up

    def short_card_details(self):
        """If card is currently face-up, returns shorthand card details; if face-down returns a consistent string."""
        if self._face_up:
            return f"{self._rank_short}-{self._suit[0]}"
        else:
            return "*-*"
