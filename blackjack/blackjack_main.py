"""
This module defines the flow of actions required to play a game of blackjack.

Classes that define game objects are imported from supporting modules. The 'run()' function is called when the
module is executed as a script. This function initiates a game of blackjack and loops through the required flow of
actions to keep the game running until the user quits or their balance reaches zero. Repeating sequences of actions,
e.g. a single round, are defined in their own functions to improve readability: these are called as necessary from
'run()'.

Attributes
----------
number_of_decks : int
    The number of 52-card decks that are shuffled into the dealer's deck object. This applies to the initial deck
    created at the start of the game and any subsequent decks created when the previous decks runs out of cards.
    Casinos normally use 6 decks at a time.
deck_length_limit : int
    When the number of cards in the deck falls below this limit, a new deck of card objects is created and shuffled.
exit_string : str
    If this string is entered by the user, the user exits the game.
"""

from blackjack import Player, Deck, DealerHand, PlayerHand
import sys
import time

number_of_decks = 6
deck_length_limit = 60
exit_string = "quit"


def run():
    """
    Controls the flow of the blackjack game based on user actions and outcomes. Call 'blackjack_main.py' to execute.

    First, a welcome message is printed then the player object is initialised, prompting the user to enter their name.
    A deck is then created; the while loop continues to invoke single rounds of blackjack: one after another. If the
    player's balance reaches zero, the loop is escaped and the game ends with a game over message. The while loop also
    checks the number of cards left in the deck before initiating another round: if the number of cards drops below a
    threshold value, a new deck is shuffled for use in subsequent rounds.
    """
    print_welcome_message()
    player_one = Player()
    game_deck = Deck(number_of_decks)
    while player_one.get_balance() > 0:
        time.sleep(1)
        if len(game_deck) < deck_length_limit:
            game_deck.new_deck()
            print_new_deck_message()
        else:
            print_new_round_message()

        single_round(
            game_deck, player_one
        )  # This starts the first round of the game, providing the above deck and player objects as input args

    print_game_over_message(player_one)


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
    players_hand = PlayerHand(player_one)  # Initialises a hand object for the player
    dealers_hand = (
        DealerHand()
    )  # Initialises a hand object for the computer-controlled dealer

    # Record player balance at start of the round
    round_start_balance = player_one.get_balance()

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
        print_balance_difference(player_one, round_start_balance)
        return

    # While loop prompts the user for actions until they 'stand' or go bust
    while players_hand.is_active():
        single_player_action(live_deck, players_hand)
        dealers_hand.print_hand()
        players_hand.print_hand()

    time.sleep(1)

    # If-Else blocks resolve the round by comparing player and dealer hand values and paying-out to players if required
    if players_hand.is_bust():
        # Player immediately loses bet (discarded with their hand); exit this round without resolving dealers hand
        print("You've gone bust!")
        time.sleep(1)
    else:
        player_score_message = f"Your score = {players_hand.best_hand_value()}"
        dealers_hand.resolve_hand(live_deck, players_hand, player_score_message)
        dealers_hand.settle_bet(players_hand, player_one)

    print_balance_difference(player_one, round_start_balance)


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
        if action_key.lower() == exit_string:
            sys.exit()
        elif action_key.lower() == "h" or action_key.lower() == "s":
            break
        print("Invalid action: please enter 'h' to hit or 's' to stand...")

    if action_key.lower() == "h":
        live_player_hand.draw_card(live_deck)
    else:
        live_player_hand.stand()


def print_welcome_message():
    """Prints a welcome message when the user starts the game."""
    print(
        "\n---------------------"
        "\nLET'S PLAY BLACKJACK!"
        "\n---------------------"
        "\n\nType 'quit' at any time to exit."
    )


def print_game_over_message(player_obj):
    """
    Prints a game over message when the user has zero balance.

    Parameters
    ----------
    player_obj : blackjack.player.Player
        The player object with balance that has reached zero. The message informs this player that they are out.
    """
    print(
        f"\n\n---------"
        f"\nGAME OVER"
        f"\n---------"
        f"\nSorry {player_obj.get_name()}, looks like you're out of money...\n"
    )


def print_new_deck_message():
    """Prints a message when the dealer shuffles a new deck before beginning a new round."""
    print("\n---------------------"
          "\nNEW ROUND - NEW DECK!"
          "\n---------------------")


def print_new_round_message():
    """Prints a message to communicate the start of a new round."""
    print("\n---------"
          "\nNEW ROUND"
          "\n---------")


def print_balance_difference(player_obj, round_start_balance):
    """Prints difference in player balance between the start and the end of the round i.e. prints winnings/losses.

    Parameters
    ----------
    player_obj : blackjack.player.Player
        The player object for which change in balance across the round is calculated/printed.
    round_start_balance : float
        The balance associated with 'player_obj' at the start of the current round.
    """
    round_balance_diff = player_obj.get_balance() - round_start_balance
    if round_balance_diff < 0:
        diff_sign = "-"
    else:
        diff_sign = "+"
    print(
        f"\n({diff_sign} {player_obj.get_currency()}{abs(round_balance_diff):.{player_obj.get_precision()}f})"
    )


if __name__ == "__main__":
    run()
