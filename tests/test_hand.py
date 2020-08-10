""" Tests for hand objects. Run using: python -m pytest"""

import pytest
from blackjack.hand import Hand


def test_hand_value_three_ten(hand_13_fixture):
    assert hand_13_fixture.calculate_hand_value() == [13]


def test_hand_value_single_ace(single_ace_fixture):
    assert single_ace_fixture.calculate_hand_value() == [11, 21]


def test_hand_value_double_ace(double_ace_fixture):
    assert double_ace_fixture.calculate_hand_value() == [2, 12, 22]


def test_hand_value_quad_ace(quad_ace_fixture):
    assert quad_ace_fixture.calculate_hand_value() == [4, 14, 24, 34, 44]
