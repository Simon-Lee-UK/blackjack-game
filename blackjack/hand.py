"""
This module exports the 'Hand' class and related methods.
"""


class Hand:
    """
    A class defining the properties and methods of a hand object.

    A hand object is a collection of cards associated with either the dealer or the player. Within a round of blackjack,
    cards are added to a hand when the associated player chooses to 'hit'. The outcome of each round is determined by
    the relative values of the player's and dealer's hands.
    """

    def __init__(self, holder_role):
        """
        Initialises an empty hand object for a given participant.

        Parameters
        ----------
        holder_role : str
            Defines the owner, or 'holder', of the hand object being created: either 'Player' or 'Dealer'
        """
        self._live_hand = (
            []
        )  # A list of card objects making up the hand; initialised as an empty list
        self._holder_role = holder_role

    def __iter__(self):
        for card in self._live_hand:
            yield card

    def __repr__(self):
        return self.print_hand()

    def __len__(self):
        return len(self._live_hand)

    @property
    def hand_value(self):
        """Returns the total value(s) of the target hand by summing the values of all constituent card objects."""
        ace_count = 0
        ace_values = None
        face_down_count = 0
        non_ace_sum = 0

        # Loop: counts number of face-down cards in the hand; counts face-up aces; sums face-up cards that aren't an ace
        for card in self._live_hand:
            # Try statement catches TypeErrors thrown when 'is_ace' method encounters a face-down card
            try:
                if card.is_ace():
                    ace_count += 1
                    ace_values = card.card_value()
                else:
                    non_ace_sum += card.card_value()
            except TypeError:
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
            face_down_value_list = [
                str(value) + " + *-*" * face_down_count for value in hand_value_list
            ]
            return face_down_value_list
        else:
            return hand_value_list

    def draw_card(self, deck_obj, face_dir):
        """
        Removes one card from the input deck and adds this card to the hand with orientation defined by 'face_dir'.

        Calls the 'deal_card' method of an input deck object, the deck returns a single card object and deletes this
        card from the deck. If the 'face_dir' input argument requires the hand to be dealt face-down, the freshly
        drawn card (face-up by default) calls its 'flip_card' method to ensure the card is correctly face-down before it
        it is appended to the hand array.

        TODO: Create a method 'hit' which just calls this method with card always face-up
        TODO: Alternatively? Rename this method to 'hit' and give face_dir a default value of 'up'

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
        empty_string = ""  # Returning an empty string lets us call this method from __repr__ and separates w/ newline
        print(f"\n{self._holder_role}'s hand")
        for idx, single_card in enumerate(self._live_hand):
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
            A two-element tuple containing the possible card values an ace can take e.g. (1, 11)

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
