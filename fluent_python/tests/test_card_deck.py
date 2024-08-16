import pytest

from .fixtures import (
    create_deck,
)
from fluent_python.card_deck import Card


class TestFrenchDeck:
    def test_deck_length(self, create_deck):
        assert len(create_deck) == 52

    @pytest.mark.parametrize(
        "expected_rank, expected_suit",
        [
            ('2', 'spades'),
        ]
    )
    def test_first_card(self, create_deck, expected_rank, expected_suit):
        assert create_deck[0] == Card(expected_rank, expected_suit)

    @pytest.mark.parametrize(
        "expected_rank, expected_suit",
        [
            ('A', 'hearts'),
        ]
    )
    def test_last_card(self, create_deck, expected_rank, expected_suit):
        assert create_deck[51] == Card(expected_rank, expected_suit)
