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
