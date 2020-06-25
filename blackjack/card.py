"""This module contains the 'Card' class and related methods.
"""


class Card:
    """ A class defining the properties of a card object. On initialisation, the internal attributes for the suit, rank,
    value and deck number of the Card are defined based on the input variables. By default, cards are created face up.
    """

    def __init__(
        self, input_suit, input_rank, input_rank_short, input_value, input_deck_num
    ):
        self._suit = input_suit
        self._rank = input_rank
        self._rank_short = input_rank_short
        self._value = input_value
        self._deck_num = input_deck_num + 1
        self._face_up = True  # This logical stores whether the card is face up (True) or face down (False)

    def print_card_details(self):
        """ Prints the key attributes of a Card object, e.g.: 'Ace of diamonds (Value = 1 or 11, Deck# = 3)'
        """
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
        """ 'Flips' the card object by setting '_face_up' to the opposite boolean value
        """
        self._face_up = not self._face_up

    def card_value(self):
        """ Returns the value of the target card. Value can be a tuple (for an Ace) or an integer value (all other
        cards).
        """
        if self._face_up:
            return (
                self._value
            )
        else:
            return "*-*"

    def is_face_up(self):
        """ Returns the current card orientation as a boolean (face-up = True, face-down = False)
        """
        return self._face_up

    def short_card_details(self):
        """ If card is currently face-up, returns details in shorthand notation, e.g.: 'K-H' denoting the King of
        hearts. If card is face-down, returns a consistent string to communicate this to the player."""
        if self._face_up:
            return f"{self._rank_short}-{self._suit[0]}"
        else:
            return "*-*"
