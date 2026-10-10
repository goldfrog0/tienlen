#!/usr/bin/env python
from typing import Iterable, List
import pytest
from rules import Kind, beats, classify
from card import Card
from constants import (SUITS, RANKS)

@pytest.mark.parametrize("cards, expected", [
    pytest.param([Card("2", "Spades")], Kind.SINGLE, id="Single"),
    pytest.param([Card("2", "Spades"), Card("2", "Hearts")], Kind.DOUBLE, id="Double"),
    pytest.param([Card("4", "Hearts"), Card("4", "Diamonds"), Card("4", "Spades")], Kind.TRIPLE, id="Triple"),
    pytest.param([Card("4", "Hearts"), Card("4", "Diamonds"), Card("4", "Spades"), Card("4", "Clubs")], Kind.QUAD, id="Quad"),
    pytest.param([Card("5", "Hearts"), Card("3", "Diamonds"), Card("4", "Spades"), Card("5", "Clubs")], None, id="3-4-5-5 fake Run"),
    pytest.param([Card("3", "Hearts"), Card("4", "Diamonds"), Card("5", "Spades"), Card("6", "Clubs")], Kind.RUN, id="3-4-5-6 Run"),
    pytest.param([Card("3", "Hearts"), Card("4", "Diamonds"), Card("5", "Spades"), Card("6", "Clubs"),
                  Card("7", "Hearts"), Card("8", "Hearts"), Card("9", "Hearts"), Card("10","Hearts"),
                  Card("Jack","Hearts"), Card("Queen", "Hearts"), Card("King", "Hearts"), Card("Ace","Hearts")], Kind.RUN, id="3-4-5-6-7-8-9-J-Q-K-A Run"),
    pytest.param([], None, id="Empty selection"),
    pytest.param([Card("4", "Hearts"), Card("4", "Diamonds"), Card("3", "Spades")], None, id="Non-matching set of three"),
    pytest.param([Card("3", "Hearts"), Card("4", "Diamonds"), Card("5", "Spades")], Kind.RUN, id="3 Card Run"),
    pytest.param([Card("3", "Hearts"), Card("4", "Diamonds"), Card("2", "Spades")], None, id="3 Card Run with a 2"),
])
def test_classify(cards, expected):
    assert classify(cards) == expected


def make_run(high_card: int, length: int, suit: str) -> List[Card]:
    made_run = []
    for i in range(high_card-length,high_card+1):
        made_run.append(Card(RANKS[i], suit))
    return made_run

TEST_TRIPLE_4 = [Card("4", "Hearts"), Card("4", "Diamonds"), Card("4", "Spades")]
TEST_TRIPLE_3 = [Card("3", "Hearts"), Card("3", "Diamonds"), Card("3", "Spades")]

TEST_RUN_3_10 = make_run(7, 3, "Hearts")
TEST_RUN_3_9 = make_run(6, 3, "Diamonds")

TEST_RUN_4_10 = make_run(7, 4, "Hearts")
TEST_RUN_4_9 = make_run(6, 4, "Diamonds")
    
@pytest.mark.parametrize("card_state, expected",[
    pytest.param((TEST_TRIPLE_4,TEST_TRIPLE_3), True, id="basic pair comp"),
    pytest.param((TEST_TRIPLE_3,TEST_TRIPLE_4), False, id="basic pair comp, reverse"),
    pytest.param((TEST_RUN_3_9, TEST_RUN_3_10), False, id="playing lesser run vs higher run"),
    pytest.param((TEST_RUN_3_10, TEST_RUN_3_9), True, id="standard higher 3 card run vs lesser"),
    pytest.param((TEST_RUN_4_10, TEST_RUN_4_9), True, id="4 card run comparison, no face cards"),
    pytest.param((TEST_RUN_4_9, TEST_RUN_4_10), False, id="4 card run comparison, no face cards, reverse"),
    pytest.param((TEST_RUN_4_10, TEST_RUN_3_9), False, id="4 card run vs 3 card run"),
])
def test_beats(card_state, expected):
    play, pile = card_state
    assert beats(play, pile) == expected
