""" Tests for hand objects. Run using: python -m pytest. """

import pytest
from blackjack.hand import Hand


def test_hand_value_three_ten(hand_13_fixture):
    assert hand_13_fixture.hand_value == [13]


def test_hand_value_single_ace(hand_1ace_fixture):
    assert hand_1ace_fixture.hand_value == [11, 21]


def test_hand_value_double_ace(hand_2ace_fixture):
    assert hand_2ace_fixture.hand_value == [2, 12, 22]


def test_hand_value_quad_ace(quad_ace_fixture):
    assert quad_ace_fixture.hand_value == [4, 14, 24, 34, 44]

def test_facedown_hand_value(hand_facedown_fixture):
    assert hand_facedown_fixture.hand_value == ["3 + *-*"]
