#!/usr/bin/env python

from card import Card
from typing import Iterable
from enum import Enum, auto

class Kind(Enum):
    SINGLE = auto()
    DOUBLE = auto()
    TRIPLE = auto()
    QUAD = auto()
    RUN = auto()

KIND_BY_RANK_COUNT = {
    1: Kind.SINGLE,
    2: Kind.DOUBLE,
    3: Kind.TRIPLE,
    4: Kind.QUAD
    
}
    
def classify(cards: Iterable[Card]) -> Kind | None:
    cards = sorted(cards)
    indices = {card.rank_index for card in cards}
    if cards:
        if len(indices) == 1:
            return KIND_BY_RANK_COUNT[len(cards)]
        else:
            return None
    else:
        return None

def main():
    test_card1 = Card("Ace", "Diamonds")
    test_card2 = Card("Ace", "Spades" )
    test_card3 = Card("3", "Clubs")

    set_cards = []

    print(classify(set_cards))

if __name__ == "__main__":
    main()


