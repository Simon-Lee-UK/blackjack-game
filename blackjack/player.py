"""
This module exports the 'Player' class and related methods.
"""
import sys

exit_string = "quit"  # If this string is entered by the user, the user exits the game.


class Player:
    """
    A class defining the properties and methods of a user-player object.

    A player object represents a single participant in the game of blackjack. A player is initialised with: a name
    (input by the user) and a starting balance of £500. Money is withdrawn from a player's balance when they make a bet;
    any winnings are paid into this balance.
    """

    def __init__(self):
        """Initialises a player object: user is required to enter a name for the player - players start with £500."""
        self._name = "None Entered"  # The player's name: requiring user keyboard input via method called below
        self.set_name()
        self._balance = 500.00  # The starting balance for any player
        self._precision = 2  # The precision (after decimal place) to which monetary amounts are rounded
        self._currency = "£"  # The currency associated with the player object's balance

    def __repr__(self):
        """
        Entering the reference for a player object in the terminal triggers this method, printing all player details.

        Returns
        -------
            Output of 'print_player_details' method : str
                Prints the player name followed by their game balance.
        """
        return self.print_player_details()

    def get_name(self):
        """Returns the player's name."""
        return self._name

    def set_name(self):
        """Sets the player's name via keyboard input from user: valid names are between 1 and 12 characters long."""
        while True:
            player_name = input("\nEnter your name: ")
            if player_name.lower() == exit_string:
                sys.exit()
            elif len(player_name) in range(1, 13):
                break
            print("Invalid name (Max length = 12 characters)")
        self._name = player_name

    def get_balance(self):
        """Returns the player's balance as a float."""
        return self._balance

    def update_balance(self, difference):
        """
        Updates the player's balance by the 'difference' input as an argument.

        Parameters
        ----------
        difference : float
            The value added (if +ve) or removed (if -ve) from the player's balance.
        """
        self._balance += difference

    def get_precision(self):
        """Returns the post-decimal precision that player balance will be quoted to."""
        return self._precision

    def get_currency(self):
        """Returns the currency associated with the player's balance."""
        return self._currency

    def place_bet(self, player_hand):
        """
        Processes a bet made by a player: user enters bet amount; amount is verified; if OK, bet is added to input hand.

        Parameters
        ----------
        player_hand : blackjack.hand.PlayerHand
            The player's 'live' hand object. The user-entered bet will be linked to this hand.
        """
        invalid_bet_message = f"Invalid bet: must be number between 0 and {self._currency}{self._balance:.2f}!"
        self.print_player_details()
        while True:
            try:
                input_amount = input(f"\nPlace your bet: ")
                amount = round(
                    float(input_amount.replace(self._currency, "")), self._precision
                )
                if 0 < amount <= self.get_balance():
                    break
                print(invalid_bet_message)
            except ValueError:
                if input_amount.lower() == exit_string:
                    sys.exit()
                print(invalid_bet_message)

        self._balance -= amount
        player_hand.add_bet(amount)

    def print_player_details(self):
        """
        Prints the player name followed by their game balance.

        Returns
        -------
        empty_string : str
            An empty string, returned so that the 'print_player_details' method can be called by the Player class'
            __repr__ method which must return a string-like object.
        """
        empty_string = ""
        print(f"{self._name}: balance = {self._currency}{self._balance:.{self._precision}f}")
        return empty_string
