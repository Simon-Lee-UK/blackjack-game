"""
This module exports the 'Hand' class, 'PlayerHand' and 'DealerHand' subclasses, and related methods.
"""
import time

draw_delay = 1  # The pause in seconds between drawn card actions
twenty_one = 21  # Ideal score value for both players


class Hand:
    """
    A class defining the properties and methods of a hand object.

    A hand object is a collection of cards associated with either the dealer or a player (each having their own 
    respective subclasses with specialised methods and attributes). Within a round of blackjack, cards are added to a 
    hand when the associated player chooses to 'hit'. The outcome of each round is determined by the relative values 
    of the player's and dealer's hands.
    """

    def __init__(self, holder_name="Player"):
        """
        Initialises an empty hand object for a given participant.

        Parameters
        ----------
        holder_name : str
            Defines the owner, or 'holder', of the hand object bseing created: either 'Player' or 'Dealer'.
            Defaults to 'Player' for this base hand class.
        """
        self._live_hand = (
            []
        )  # A list of card objects making up the hand; initialised as an empty list
        self._active = True  # The active status communicates whether the hand is still active in the current round
        self._bust = False  # The bust status communicates whether the hand is bust (value > 21) in the current round
        self._natural = False  # The natural status communicates whether the hand is a natural (value = 21 with 2 cards)
        self._holder_name = holder_name

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

    def hand_value(self, bypass_face_down=False):
        """
        Returns the total value(s) of the target hand by summing the values of all constituent card objects.

        Parameters
        ----------
        bypass_face_down : bool
            Tells method whether to include face-down cards in calculating the value(s) of the hand. Defaults to False.

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
            # Try statement catches AssertionErrors thrown when 'is_ace' method encounters a face-down card
            try:
                if card.is_ace(bypass_face_down):
                    ace_count += 1
                    ace_values = card.card_value(bypass_face_down)
                else:
                    non_ace_sum += card.card_value(bypass_face_down)
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

    def best_hand_value(self):
        """
        Returns the best possible value of the hand as an integer. If hand value is bust (> 21), returns None.

        Returns
        -------
        best_value : int or None
            The best possible total value of the hand's constituent cards. If no hand value <= 21, 'best_value' = None.
        """
        max_best_value = 21
        all_hand_values = self.hand_value(bypass_face_down=True)
        try:
            best_value = max([val for val in all_hand_values if val <= max_best_value])
        except ValueError:
            best_value = None

        return best_value

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

    def is_natural(self):
        """
        As a boolean, returns 'natural' status of hand (2 cards in hand and value = 21: returns True; otherwise False).

        Returns
        -------
        bool
            True when card contains two cards with combined value of 21; otherwise False.
        """
        return self._natural

    def stand(self):
        """Updates hand status to inactive: triggered when player chooses to draw no more cards in the current round."""
        self._active = False

    def draw_card(self, deck_obj, face_dir="up"):
        """
        Removes one card from the input deck and adds this card to the hand with orientation defined by 'face_dir'.

        Calls the 'deal_card' method of an input deck object, the deck returns a single card object and deletes this
        card from the deck. If the 'face_dir' input argument requires the hand to be dealt face-down, the freshly
        drawn card (face-up by default) calls its 'flip_card' method to ensure the card is correctly face-down before it
        it is appended to the hand array. Finally, the method calls '_validate_hand_status' that checks whether the hand
        is now bust and updates all hand statuses accordingly.

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
        assert (
            self.is_active()
        ), "Cannot draw a card to this hand: it is marked as inactive in the current round."
        drawn_card = deck_obj.deal_card()
        if face_dir.lower() != "up":
            drawn_card.flip_card()
        self._live_hand.append(drawn_card)
        self._verify_hand_status()

    def print_hand(self, alt_text=None):
        """
        Prints the hand's owner followed by shorthand details of all cards currently within the hand.

        Parameters
        ----------
        alt_text : str
            This optional argument will be printed instead of the hand owner's name if provided.

        Returns
        -------
        empty_string : str
            An empty string, returned so that the 'print_hand' method can be called by the Hand class' __repr__
            method which must return a string-like object.
        """
        empty_string = ""
        ends_with_s = self._holder_name[-1].lower() == "s"

        if alt_text is not None:
            print(alt_text)
        elif ends_with_s:
            print(f"\n{self._holder_name}' hand")
        else:
            print(f"\n{self._holder_name}'s hand")

        for idx, single_card in enumerate(self):
            print(f"Card {idx}: {single_card.short_card_details()}")

        if (
            self.is_active()
            or self.is_bust()
            or (self.best_hand_value() == twenty_one and alt_text is not None)
        ):
            print(f"Value: {self.hand_value()}")
        return empty_string

    def _verify_hand_status(self):
        """Checks whether the hand is bust, has value equal to 21 or is a natural. Updates hand status accordingly."""
        natural_length = 2
        if self.best_hand_value() is None:
            self._bust = True
            self.stand()
        elif self.best_hand_value() == twenty_one:
            self.stand()
            if len(self) == natural_length:
                self._natural = True

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

    def resolve_hand(self, deck_obj, player_hand, player_score_message):
        """
        This method automatically resolves the dealer's hand: drawing cards until the hand value exceeds seventeen.

        Method initially checks the dealer's hand value: if its best value > 17, the dealer stands. If < 17, the hand
        draws cards until its value exceeds 17 or goes bust. The dealer's final hand score is printed to the screen
        or the player is informed that the dealer has gone bust.

        Parameters
        ----------
        deck_obj : blackjack.deck.Deck
            The game's 'live' deck object - cards may be removed from this deck and added to the dealer's hand object.
        player_hand : blackjack.hand.PlayerHand
            A player's 'live' hand object. Allows the player's hand to be printed for comparison as the dealer's hand is
            resolved.
        player_score_message : str
            A string that communicates the players score. As the dealer's hand is resolved, the players score is
            printed each time the dealer's hand is printed so the user can easily compare the relative scores.
        """
        dealer_target = 17
        print(player_score_message)
        if player_hand.best_hand_value() == twenty_one:
            print("You've got 21!")
            time.sleep(draw_delay)

        self._reveal_hand()

        while self.is_active():
            if self.best_hand_value() < dealer_target:
                self.draw_card(deck_obj)
                self.print_hand(alt_text="\nDealer hits:")
                player_hand.print_hand()
                print(player_score_message)
                print("\n---")
                time.sleep(draw_delay)
            else:
                self.stand()
                self.print_hand(alt_text="\nDealer stands:")
                print(f"Dealer's score = {self.best_hand_value()}")
                player_hand.print_hand()
                print(player_score_message)
                break

        if self.is_bust():
            self.print_hand(alt_text="\nDealer has gone bust!")
            player_hand.print_hand()
            print(player_score_message)
            print("\n---")

    def _reveal_hand(self):
        """Turns all cards in the hand face-up and prints hand details to the screen."""
        print("\n---------------")
        for card in self:
            if not card.is_face_up():
                card.flip_card()
        self.print_hand(alt_text="Dealer reveals hand:")
        print("---------------")
        time.sleep(draw_delay)

    def settle_naturals(self, player_hand, player_obj):
        """
        Method detects naturals and settles any bets as necessary; returns True if round is concluded, otherwise False.

        A hand is a 'natural' if it contains two cards with a total value of 21. Players and dealers can get naturals
        upon drawing their first two cards at the start of a round. If the dealer gets a natural, the round is over and
        they collect the bet of any player who did not also get a natural. If a player gets a natural and the dealer did
        not, they are immediately paid 1.5x the value of their bet.

        Parameters
        ----------
        player_hand : blackjack.hand.PlayerHand
            A player's 'live' hand object. The 'natural' status of this hand is read and compared to the status of the
            dealer's hand. Where a payout is required, the amount bet against the hand is also read into 'bet_amount'.
        player_obj : blackjack.player.Player
            The player object that owns the input 'player_hand'. Where a payout is required, this player's balance
            will be updated accordingly.

        Returns
        -------
        round_complete : bool
            Returns True if no further actions are possible in the current round, following the settling of naturals;
            otherwise False (and the round continues).
        """
        if not any((self.is_natural(), player_hand.is_natural())):
            round_complete = False
            return round_complete
        else:
            round_complete = True
            bet_amount = player_hand.get_bet()

        if self.is_natural() and not player_hand.is_natural():
            # No action, round ends and bet is collected (discarded) automatically with player's hand
            self._reveal_hand()
            print("Dealer has a natural!")
        elif not self.is_natural() and player_hand.is_natural():
            # Player wins 1.5x their original bet; multiplier is 2.5x so bet amount is also deposited back into balance
            print(f"\n{player_obj.get_name()} has a natural (dealer does not)!")
            payout_multiplier = 2.5
            player_obj.update_balance(bet_amount * payout_multiplier)
        elif all((self.is_natural(), player_hand.is_natural())):
            # Stand-off between player and dealer: player's bet is deposited back into balance
            print(f"\n{player_obj.get_name()} has a natural!")
            self._reveal_hand()
            print("\nSo does the dealer! It's a stand-off!")
            payout_multiplier = 1
            player_obj.update_balance(bet_amount * payout_multiplier)

        return round_complete

    def settle_bet(self, player_hand, player_obj):
        """
        Method settles any bets at the end of the round; where the player loses, the method exits and their bet is lost.

        The value of the dealer's and player's hands are compared. If the player wins, their player object is payed the
        value of their bet plus the original bet amount is returned. If it's a draw, the bet is returned to the player's
        balance but they receive no winnings. If the player loses, the method exits and their balance is uneffected.
        The bet placed against their hand is lost when a new round starts and new hands are initialised.

        Parameters
        ----------
        player_hand : blackjack.hand.PlayerHand
            A player's 'live' hand object. The value of this hand is read and compared to the value of the
            dealer's hand. Where a payout is required, the amount bet against the hand is also read into 'bet_amount'.
        player_obj : blackjack.player.Player
            The player object that owns the input 'player_hand'. Where a payout is required, this player's balance
            will be updated accordingly.
        """
        assert not any(
            (self.is_active(), player_hand.is_active())
        ), "Bets cannot be settled between the dealer and a player unless both participants have 'stood' or gone bust."

        if player_hand.is_bust():
            return
        if self.is_bust():
            dealer_score = 0
        else:
            dealer_score = self.best_hand_value()

        if dealer_score > player_hand.best_hand_value():
            return
        else:
            bet_amount = player_hand.get_bet()

        if player_hand.best_hand_value() > dealer_score:
            payout_multiplier = 2
            player_obj.update_balance(bet_amount * payout_multiplier)
        elif player_hand.best_hand_value() == dealer_score:
            payout_multiplier = 1
            player_obj.update_balance(bet_amount * payout_multiplier)


class PlayerHand(Hand):
    """
    A subclass defining the properties and methods specific to a hand object held by a player.

    Players' hands are special because bets can be made against these hands.
    """

    def __init__(self, player_obj):
        """
        Calls the __init__ method of the base Hand class, initialising an empty hand object for the player.

        Parameters
        ----------
        player_obj : blackjack.player.Player
            The player object that owns the hand being initialised. The name of this player is queried and set
            used to define the '_holder_name' attribute on the base class. This name is then displayed when printing
            hand details to screen.
        """
        self._bet = float(
            0
        )  # An attribute holding the amount bet by a player against this hand: initially zero
        player_name = player_obj.get_name()
        super().__init__(player_name)

    def add_bet(self, amount):
        """
        Adds a bet made by a player to the current hand object: at the end of a round, the dealer resolves this bet.

        Parameters
        ----------
        amount : float
            The amount bet against the hand object. In typical game flow, this bet amount has already been verified
            as positive and has already been removed from the player's balance.
        """
        self._bet += amount

    def get_bet(self):
        """Returns the amount bet against this player's hand as a float."""
        return self._bet
