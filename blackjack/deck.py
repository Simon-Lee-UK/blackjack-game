"""
This module exports the 'Deck' class and related methods.
"""
from blackjack import Card
from random import shuffle


class Deck:
    """
    A class defining the properties and methods of a deck object.

    A single deck object contains one or more 52-card sets of playing card objects. In each round of blackjack,
    cards are dealt from the deck to the dealer and player's hands. Cards dealt from the deck are not shuffled back
    in: when the deck size drops below a defined limit, a fresh shuffled deck object can be created to replace it using
    the new_deck() method.
    """

    def __init__(self, input_deck_count):
        """
        Initialises a shuffled deck object.

        Parameters
        ----------
        input_deck_count : int
            The number of 52-card sets to be shuffled into a deck object on initialisation.
        """
        self._live_deck = (
            []
        )  # The list of card objects making up the deck: populated on initialisation by new_deck()
        self._suit_names = (
            "Spades",
            "Hearts",
            "Clubs",
            "Diamonds",
        )  # The four suits found in a pack of cards
        self._rank_names = (
            "Ace",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Jack",
            "Queen",
            "King",
        )  # The thirteen ranks of card within each suit
        self._rank_short = (
            "A",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K",
        )  # Equivalent tuple of shortened rank names (useful for displaying as text to player)
        self._rank_values = (
            (1, 11),
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            10,
            10,
            10,
        )  # The 13 card values in blackjack

        self._validate_deck_count(input_deck_count)
        self._deck_count = input_deck_count
        self.new_deck()

    def __iter__(self):
        """
        Allows deck objects to be iterated over, yielding constituent card objects in order from top of deck to bottom.

        Yields
        ------
            card : blackjack.card.Card
                The next card in the deck (within the deck object's '_live_deck' attribute).
        """
        for card in self._live_deck:
            yield card

    def __repr__(self):
        """
        Entering the reference for a deck object in the terminal calls this method, printing details of all deck cards.

        Returns
        -------
            Output of 'print_deck' method : str
                Prints verbose details of all cards within the deck object (top to bottom).
        """
        return self.print_deck()

    def __len__(self):
        """Allows len() to be used on deck objects, returning the number of cards in the deck as the object 'length'."""
        return len(self._live_deck)

    def new_deck(self):
        """
        Loops through a deck object's attribute tuples to populate the '_live_deck' with one or more sets of 52 cards.

        The game deck is populated with an integer number of full 52-card sets, set by the '_deck_count' attribute.
        Once the game deck has been created, another 'Deck' method: 'shuffle_deck' is called to randomly order the
        card objects within the list, giving a shuffled deck to start or continue the game.
        """
        self._live_deck.clear()  # This line clears any existing elements from the '_live_deck' list - only required
        # when calling the method against an existing 'Deck' object, e.g.: " some_deck_object.new_deck() " would
        # effectively clear-out the existing deck, replacing it with a fresh one
        for deck_number in range(self._deck_count):
            for suit in self._suit_names:
                for (rank, rank_short, rank_value) in zip(
                    self._rank_names, self._rank_short, self._rank_values
                ):
                    self._live_deck.append(
                        Card(suit, rank, rank_short, rank_value, deck_number,)
                    )
        self.shuffle_deck()  # Calls the 'shuffle_deck' method against the current Deck object

    def shuffle_deck(self):
        """Applies a new random ordering to the card objects contained within a deck object."""
        shuffle(self._live_deck)

    def deal_card(self):
        """
        Returns and removes the top card from the deck object's '_live_deck'. Called by hand objects.

        Returns
        -------
        blackjack.card.Card
            The top card from the deck object is returned: it has been removed from the deck.
        """
        return self._live_deck.pop(0)

    def print_deck(self):
        """
        Prints verbose details of all cards within the deck object (top to bottom).

        Returns
        -------
        empty_string : str
            An empty string, returned so that the 'print_deck' method can be called by the Deck class' __repr__
            method which must return a string-like object.
        """
        empty_string = ""
        for card in self:
            card.print_card_details()
        return empty_string

    @staticmethod
    def _validate_deck_count(input_deck_count):
        """
        Asserts that 'input_deck_count' is a positive integer when initialising a deck object.

        Parameters
        ----------
        input_deck_count : int
            The number of 52-card sets to be shuffled into a deck object on initialisation
        """
        assert (isinstance(input_deck_count, int)) and (
            input_deck_count > 0
        ), "'input_deck_count' must be a positive integer!"
