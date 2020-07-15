""" Tests for hand objects. Run using: python -m pytest"""

import pytest
from blackjack.hand import Hand


def test_hand_value_three_ten(three_clubs_fixture, queen_spades_fixture):
    test_hand = Hand("Player")
    test_hand._live_hand.extend([three_clubs_fixture, queen_spades_fixture])
    assert test_hand.hand_value() == 13
