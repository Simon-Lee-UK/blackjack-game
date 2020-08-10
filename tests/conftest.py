""" File to create standard objects for test using pytest. """
import pytest
from blackjack.card import Card
from blackjack.hand import Hand


@pytest.fixture
def ace_spades_fixture():
    return Card("Spades", "Ace", "A", (1, 11), 0)


@pytest.fixture
def ace_diamonds_fixture():
    return Card("Diamonds", "Ace", "A", (1, 11), 0)


@pytest.fixture
def queen_spades_fixture():
    return Card("Spades", "Queen", "Q", 10, 0)


@pytest.fixture
def three_clubs_fixture():
    return Card("Clubs", "Three", "3", 3, 0)


@pytest.fixture
def hand_13_fixture(three_clubs_fixture, queen_spades_fixture):
    hand_13 = Hand("Player")
    hand_13._live_hand.extend([three_clubs_fixture, queen_spades_fixture])
    return hand_13


@pytest.fixture
def single_ace_fixture(ace_spades_fixture, queen_spades_fixture):
    hand_single_ace = Hand("Player")
    hand_single_ace._live_hand.extend([ace_spades_fixture, queen_spades_fixture])
    return hand_single_ace


@pytest.fixture
def double_ace_fixture(ace_spades_fixture, ace_diamonds_fixture):
    hand_double_ace = Hand("Player")
    hand_double_ace._live_hand.extend([ace_spades_fixture, ace_diamonds_fixture])
    return hand_double_ace


@pytest.fixture
def quad_ace_fixture(ace_spades_fixture, ace_diamonds_fixture):
    hand_quad_ace = Hand("Player")
    hand_quad_ace._live_hand.extend(
        [
            ace_spades_fixture,
            ace_diamonds_fixture,
            ace_spades_fixture,
            ace_diamonds_fixture,
        ]
    )
    return hand_quad_ace
