#!/usr/bin/env python
import pygame
import rectangle as rect
from constants import (SUITS, RANKS)

class Card(rect.RectangleShape):
    def __init__(self,
                 x: float,
                 y: float,
                 h: float,
                 w: float,
                 rank: str,
                 suit: str
                 ) -> None:
        super().__init__(x,y,h,w)
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(rank)
        self.suit_index = SUITS.index(suit)

    #def __eq__(self, other: object) -> bool:
    #    if isinstance(other, Card):
    #        return (self.rank_index == other.rank_index) and (self.suit_index == other.suit_index)
    #    else: 
    #        return False

    def __lt__(self, other: "Card") -> bool:
        if self != other:
            if self.rank_index == other.rank_index:
                return self.suit_index < other.suit_index
            else:
                return self.rank_index < other.rank_index
        return False

    def __gt__(self, other: "Card") -> bool:
        if self != other:
            if self.rank_index == other.rank_index:
                return self.suit_index > other.suit_index
            else:
                return self.rank_index > other.rank_index
        return False

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"
