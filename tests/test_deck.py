""" Tests for deck objects."""

import pytest
from blackjack import Deck


def test_single_deck_length():
    expected_length = 52
    single_deck = Deck()
    assert len(single_deck._deck_array) == expected_length
