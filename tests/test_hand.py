""" Tests for hand objects. Run using: python -m pytest"""

import pytest
from blackjack.hand import Hand


def test_hand_value_three_ten(hand_13_fixture):
    assert hand_13_fixture.hand_value() == 13
