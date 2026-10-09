#!/usr/bin/env python
import pytest
from rules import Kind, classify
from card import Card

@pytest.mark.parametrize("cards, expected", [
    pytest.param([Card("2", "Spades")], Kind.SINGLE, id="Single"),
    pytest.param([Card("2", "Spades"), Card("2", "Hearts")], Kind.DOUBLE, id="Double"),
    pytest.param([Card("4", "Hearts"), Card("4", "Diamonds"), Card("4", "Spades")], Kind.TRIPLE, id="Triple"),
    pytest.param([Card("4", "Hearts"), Card("4", "Diamonds"), Card("4", "Spades"), Card("4", "Clubs")], Kind.QUAD, id="Quad"),
    pytest.param([], None, id="Empty selection"),
    pytest.param([Card("4", "Hearts"), Card("4", "Diamonds"), Card("3", "Spades")], None, id="Non-matching set of three"),
    pytest.param([Card("3", "Hearts"), Card("4", "Diamonds"), Card("5", "Spades")], Kind.RUN, id="3 Card Run"),
    pytest.param([Card("3", "Hearts"), Card("4", "Diamonds"), Card("2", "Spades")], None, id="3 Card Run with a 2"),
])
def test_classify(cards, expected):
    assert classify(cards) == expected
