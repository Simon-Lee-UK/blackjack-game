"""
This module defines the flow of actions required to play a game of blackjack.

Classes that define game objects are imported from supporting modules. The 'main()' function is called when the
module is executed as a script. This function initiates a game of blackjack and loops through the required flow of
actions to keep the game running until the user quits. Repeating sequences of actions, e.g. a single round,
are defined in their own functions to improve readability: these are called as necessary from 'main()'.

Attributes
----------
number_of_decks : int
    The number of 52-card decks that are shuffled into the dealer's deck object. This applies to the initial deck
    created at the start of the game and any subsequent decks created when the previous decks runs out of cards.
    Casinos normally use 6 decks at a time.
face_directions : list[str]
    A list holding the two possible card orientations as strings: face-up, and face-down
"""

from blackjack import Deck
from blackjack import Hand

number_of_decks = 1
face_directions = ["up", "down"]


def main():
    """
    Controls the flow of the blackjack game based on user actions and outcomes. Call 'blackjack_main.py' to execute.

    --- Thinking about containing the game within a couple of while loops. The outer loop would just keep the game going
    until some exit command is received. The inner loop could be a while loop based on the length of the deck array.
    When the number of cards (length of array) dropped below a certain threshold value, that round would continue but
    then the loop is escaped and a totally new game deck is created to continue the game. You then re-enter this loop
    until another new deck is required. ---

    --- Current idea for hands is to have a small list of objects that is appended when dealt to and cleared out when
    the hand is discarded. Makes sense for deck objects to have a 'deal' method. How will this correctly pass cards to a
    hand? ---
    """
    first_deck = Deck(number_of_decks)
    first_deck.print_deck()  # This prints details of the cards in the deck - currently nice to check it's working OK
    single_round(
        first_deck
    )  # This starts the first round of the game, providing the above deck object as input arg


def single_round(live_deck):
    """
    Steps through a single round of blackjack: accepting user inputs as actions and manipulating objects as required.

    --- Currently, not a full round. Just deals two cards to the player and two cards to the dealer then prints both
    hands. As these hands are defined within the 'single_round' function (and are not returned at the end), they only
    exist for a single round. For now, think this is fine. When writing info to StatJack, will need to ensure hand info
    is written from this function. ---

    Parameters
    ----------
    live_deck : blackjack.deck.Deck
        The game's 'live' deck object. All cards for this single round will be dealt from this deck.

    """
    players_hand = Hand("Player")  # Initialises a hand object for the player
    dealers_hand = Hand(
        "Dealer"
    )  # Initialises a hand object for the computer-controlled dealer
    for direction in face_directions:
        players_hand.draw_card(live_deck)
        dealers_hand.draw_card(
            live_deck, direction
        )  # Loop ensures dealer's first card is face-up, second face-down
    dealers_hand.print_hand()  # Prints the dealer's hand
    players_hand.print_hand()  # Prints the player's hand


if __name__ == "__main__":
    main()
