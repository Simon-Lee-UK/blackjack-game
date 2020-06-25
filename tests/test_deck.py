""" Tests for deck objects. Run using: python -m pytest"""

import pytest
from blackjack.deck import Deck


@pytest.mark.parametrize("deck_count,multiplier", [(1, 1), (2, 2), (6, 6), (10, 10)])
def test_deck_length(deck_count, multiplier):
    expected_length = 52 * multiplier
    single_deck = Deck(deck_count)
    real_length = len(single_deck._live_deck)
    assert real_length == expected_length


@pytest.mark.parametrize(
    "deck_count,error_type",
    [
        (1.6, AssertionError),
        ("test string", TypeError),
        (-1, AssertionError),
        (0, AssertionError),
    ],
)
def test_invalid_type_deck_length(deck_count, error_type):
    with pytest.raises(error_type):
        single_deck = Deck(deck_count)
