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
"""

from blackjack import Player, Deck, DealerHand, PlayerHand
import time

number_of_decks = 1


def main():
    """
    Controls the flow of the blackjack game based on user actions and outcomes. Call 'blackjack_main.py' to execute.

    --- Thinking about containing the game within a couple of while loops. The outer loop would just keep the game going
    until some exit command is received. The inner loop could be a while loop based on the length of the deck array.
    When the number of cards (length of array) dropped below a certain threshold value, that round would continue but
    then the loop is escaped and a totally new game deck is created to continue the game. You then re-enter this loop
    until another new deck is required. ---

    --- Current idea for hands is to have a small list of objects that is appended when dealt to and cleared out when
    the hand is discarded. ---
    """
    player_one = Player()
    first_deck = Deck(number_of_decks)
    first_deck.print_deck()  # This prints details of the cards in the deck - currently nice to check it's working OK
    while True:
        time.sleep(1.5)
        print("\n---------"
              "\nNEW ROUND"
              "\n---------")
        single_round(
            first_deck, player_one
        )  # This starts the first round of the game, providing the above deck and player objects as input args


def single_round(live_deck, player_one):
    """
    Steps through a single round of blackjack: accepting user inputs as actions and manipulating objects as required.

    Defining a new hand object for each participant every round removes the need tidy-up hand statuses; clear out
    cards, etc. By reassigning the same reference to the fresh hands, we rely on Python to garbage collect old
    inaccessible hand objects.

    Parameters
    ----------
    live_deck : blackjack.deck.Deck
        The game's 'live' deck object. All cards for this single round will be dealt from this deck.
    player_one : blackjack.player.Player
        The player competing against the dealer in this round. The PlayerHand object defined below will belong to this
        player who will bet against it from their game balance. In future, this argument may be expanded to import a
        collection of players to the round.
    """
    # Initialise hands
    players_hand = PlayerHand()  # Initialises a hand object for the player
    dealers_hand = (
        DealerHand()
    )  # Initialises a hand object for the computer-controlled dealer

    # Bets are placed
    player_one.place_bet(players_hand)

    # Draws two cards each for the player and the dealer
    players_hand.draw_card(live_deck)
    dealers_hand.draw_card(live_deck)
    players_hand.draw_card(live_deck)
    dealers_hand.draw_card(live_deck)

    # Hands are printed before play commences
    dealers_hand.print_hand()  # Prints the dealer's hand
    players_hand.print_hand()  # Prints the player's hand

    # Detects and settles any naturals drawn by the dealer or player; if round is fully resolved, exits 'single_round'
    round_complete = dealers_hand.settle_naturals(players_hand, player_one)
    if round_complete:
        return

    # While loop prompts the user for actions until they 'stand' or go bust
    while players_hand.is_active():
        single_player_action(live_deck, players_hand)
        players_hand.print_hand()

    # If-Else blocks resolve the round by comparing player and dealer hand values and paying-out to players if required
    if players_hand.is_bust():
        # Player loses money (discarded with their hand); exit this round without resolving dealers hand
        print("You've gone bust!")
        return
    else:
        print(f"Your score = {players_hand.best_hand_value()}")  # remove?
        dealers_hand.resolve_hand(live_deck)
        dealers_hand.settle_bet(players_hand, player_one)


def single_player_action(live_deck, live_player_hand):
    """
    Processes one action from the player, currently: a choice between 'hit' (take a card) or 'stand' (no more cards).

    Player enters their action choice at the command line. A valid entry of 'h' = hit or 's' = stand is required before
    the function triggers the associated action against the player's hand.

    Parameters
    ----------
    live_deck : blackjack.deck.Deck
        The game's 'live' deck object. If player action requires a card to be dealt, it will be dealt from this deck.
    live_player_hand : blackjack.hand.PlayerHand
        The player's 'live' hand object. The output action (hit/stand) will be applied to this hand.
    """
    while True:
        action_key = input("\nHit [h] or Stand [s]: ")
        if action_key.lower() == "h" or action_key.lower() == "s":
            break
        print("Invalid action: please enter 'h' to hit or 's' to stand...")

    if action_key.lower() == "h":
        live_player_hand.draw_card(live_deck)
    else:
        live_player_hand.stand()


if __name__ == "__main__":
    main()
