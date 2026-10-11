#!/usr/bin/env python
from typing import Tuple
import pytest
from card import Card

# testing card behavior

TEST_CARD_2C_1 = Card("2", "Clubs")
TEST_CARD_2C_2 = Card("2", "Clubs")
TEST_CARD_2H = Card("2", "Hearts")



@pytest.mark.parametrize("cards, expected", [
    pytest.param((TEST_CARD_2C_1, TEST_CARD_2C_2), True, id="tests seperately created cards are equal"),
    pytest.param((TEST_CARD_2C_1, TEST_CARD_2H), False, id="tests cards with same rank, different suit are not equal")
])

def test_card_equality(cards, expected):
    card1, card2 = cards
    assert (card1 == card2) == expected

@pytest.mark.parametrize("cards, expected", [
    pytest.param({TEST_CARD_2C_1, TEST_CARD_2C_2}, 1, id="tests set of same cards properly gets shrunk")
])
def test_len_card_set(cards, expected: int):
    assert len(cards) == expected

@pytest.mark.parametrize("cards, expected", [
    pytest.param((TEST_CARD_2C_1, TEST_CARD_2C_2), True, id="tests hash of diff cards with same rank and suit are the same"),
    pytest.param((TEST_CARD_2C_1, TEST_CARD_2H), False, id="tests hash of diff cards, diff suit are different"),
])
def test_card_hash(cards, expected: bool):
    card1, card2 = cards
    assert (hash(card1) == hash(card2)) == expected
