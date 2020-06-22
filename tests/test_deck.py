""" Tests for deck objects."""

import pytest
from blackjack.deck import Deck


def test_single_deck_length():
    expected_length = 52
    single_deck = Deck()
    real_length = len(single_deck._deck_array)
    assert real_length == expected_length
