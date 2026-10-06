#!/usr/bin/env python

import random
from card import (Card)
from constants import (SUITS,RANKS)

class Deck():
    def __init__(self, seed: int | None=None) -> None:
        self.seed = seed

        if seed is None:
            self.seed = random.randint(0,100000000)
        self._rng = random.Random(self.seed)
        
        self.deck_stack: list[Card] = []
        for rank in RANKS:
            for suit in SUITS:
                self.deck_stack.append(Card(rank, suit))

    def __str__(self) -> str:
        stack = ""
        for card in self.deck_stack:
            stack += f"{card}\n"
        return stack

    def shuffle(self):
        self._rng.shuffle(self.deck_stack)

def main():
    test = Deck(seed = None)
    print(test)
    test.shuffle()
    print(test)
    test.deck_stack = sorted(test.deck_stack)
    print(test)
if __name__ == "__main__":
    main()
