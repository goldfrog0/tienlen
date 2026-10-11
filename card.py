#!/usr/bin/env python
from constants import (SUITS, RANKS)

class Card():
    def __init__(self,
                 rank: str,
                 suit: str
                 ) -> None:
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(rank)
        self.suit_index = SUITS.index(suit)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        else: 
           return (self.rank_index == other.rank_index) and (self.suit_index == other.suit_index)

    def __hash__(self) -> int:
        return hash((self.rank, self.suit))

    def __lt__(self, other: "Card") -> bool:
        if self.rank_index == other.rank_index:
            return self.suit_index < other.suit_index
        else:
            return self.rank_index < other.rank_index
        
    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def __repr__(self) -> str:
        return f"Card({self.rank!r}, {self.suit!r})"
