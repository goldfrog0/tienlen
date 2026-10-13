#!/usr/bin/env python

import pytest
from game import Game
from card import Card
from hand import Hand

p0_hand = Hand([
    Card("3", "Spades"),
    Card("9", "Hearts"),
    Card("4", "Hearts"),
    Card("4", "Diamonds"),
    Card("Ace", "Diamonds"),
])
p1_hand = Hand([
    Card("2", "Spades"),
    Card("3", "Hearts"),
    Card("6", "Hearts"),
    Card("9", "Diamonds"),
    Card("King", "Diamonds"),
])
p2_hand = Hand([
    Card("6", "Spades"),
    Card("10", "Hearts"),
])
p3_hand = Hand([
    Card("5", "Spades"),
    Card("King", "Hearts"),
    Card("Queen", "Hearts"),
    Card("4", "Spades"),
    Card("Queen", "Diamonds"),
])

def make_game_hands():
    return [p0_hand, p1_hand, p2_hand, p3_hand]

# tests game starts correct player (holder of 3 of spades)
def test_game_starts_correct_player():
    game = Game(make_game_hands())
    assert game.current == 0

# tests game doesnt allow passing on empty pile
def test_empty_pass():
    game = Game(make_game_hands())
    assert game.pass_turn() is False

# tests player cannot play cards they dont have
def test_phantom_card_play():
    game = Game(make_game_hands())
    before = (game.current, list(game.pile), game.passed)

    assert game.play([Card("King", "Diamonds")]) is False

    after = (game.current, list(game.pile), game.passed)
    assert after == before

# test standard legal play
def test_legal_play():
    game = Game(make_game_hands())
    before_len = len(game.hands[game.current])
    truth_value = game.play(Hand([Card("3", "Spades")]))
    assert truth_value is True
    assert before_len - 1 == len(game.hands[0])
    assert game.pile_owner == 0
    assert game.current == 1
    assert list(game.pile) == [Card("3", "Spades")] 

# test illegal play is refused
def test_illegal_play():
    game = Game(make_game_hands())
    game.play(Hand([Card("3", "Spades")]))
    game.play(Hand([Card("King", "Diamonds")]))
    before_len = len(game.hands[game.current])
    truth_value = game.play(Hand([Card("6", "Spades")]))
    assert truth_value is False
    assert before_len == len(game.hands[2])
    assert game.pile_owner == 1
    assert game.current == 2
    assert list(game.pile) == [Card("King", "Diamonds")]

# test passing blocked on empty pile
def test_passing_blocked():
    game = Game(make_game_hands())
    before_len = len(game.hands[game.current])
    truth_value = game.pass_turn()
    current_after_pass = game.current
    passed = game.passed
    assert truth_value is False
    assert before_len == len(game.hands[0])
    assert game.pile_owner == None
    assert current_after_pass == 0
    assert 0 not in passed 
    
# test passing allowed with pile
def test_passing_allowed():
    game = Game(make_game_hands())
    game.play(Hand([Card("3", "Spades")]))
    truth_value = game.pass_turn()
    current_after_pass = game.current
    passed = game.passed
    assert truth_value is True
    assert game.pile_owner == 0
    assert current_after_pass == 2
    assert 1 in passed
    
# test all passing after first play, lets first play
def test_passing_all_pass():
    #p0 plays
    game = Game(make_game_hands())
    game.play(Hand([Card("3", "Spades")]))
    #p1 passes
    game.pass_turn()
    #p2 passes
    game.pass_turn()
    #p3 passes
    game.pass_turn()
    current_after_pass = game.current
    passed = game.passed
    pile = game.pile
    assert game.pile_owner is None
    assert current_after_pass == 0
    assert list(pile) == []
    assert passed == []
