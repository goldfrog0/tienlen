#!/usr/bin/env python

from hand import (Hand)
from card import (Card)
from rules import (beats)

class Game():
    def __init__(self, hands: list[Hand]) -> None:
        self.hands = hands
        for idx, hand in enumerate(self.hands):
            if hand[0] == Card("3", "Spades"):
                self.current = idx
                break
        else:
            raise ValueError("No 3 of Spades found in player's hands")
        self.pile = Hand([])
        self.pile_owner = None
        self.passed = []

    def play(self, cards) -> bool:
        for card in cards:
            if card not in self.hands[self.current]:
                return False
        if beats(cards, self.pile):
            self.pile = Hand(cards) 
            self.hands[self.current] = self.hands[self.current].without(cards)
            self.pile_owner = self.current
            self._next_turn()
            return True
        return False

    def pass_turn(self) -> bool:
        if self.pile:
            self.passed.append(self.current)
            self._next_turn()
            return True
        else:
            return False

    def _next_turn(self) -> None:
        next_player = (self.current + 1) % 4
        if next_player == self.pile_owner:
            self.pile = Hand([])
            self.passed = []
            self.pile_owner = None
            self.current = next_player
        elif next_player in self.passed:
            self.current = next_player
            self._next_turn() 
        else:
            self.current = next_player

    def check_game_over(self) -> bool:
        for hand in self.hands:
            if not hand: 
                return True
        return False
