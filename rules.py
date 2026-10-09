#!/usr/bin/env python

from card import Card
from hand import Hand
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
        match len(indices):
            case 1: # single checker
                return KIND_BY_RANK_COUNT[len(cards)]
            case n if (n <= 13 and n > 2):
                # run checker  
                neighbors = zip(sorted(list(indices)), sorted(list(indices))[1:])
                if "2" in [card.rank for card in cards]:
                    return None
                if len(indices) != len(cards):
                    return None
                neighbor_checks = []
                for a, b in neighbors:
                    neighbor_checks.append(b == a + 1) 
                return Kind.RUN if all(neighbor_checks) else None 
            case _:
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


