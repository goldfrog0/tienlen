#!/usr/bin/env python
from typing import Iterable
from hand import Hand
from card import Card
from rules import (beats, classify, Kind)
from itertools import (groupby, combinations)

def find_lowest_beat(bot_hand: Hand, current_pile: Hand) -> Iterable[Card] | None:
    hand_kind = classify(current_pile)
    #works assuming incoming bot_hand is already sorted.
    #might add a guard later 
    match hand_kind:
        case Kind.SINGLE:
            for card in bot_hand:
                if beats([card], current_pile):
                    return [card]
        case Kind.DOUBLE | Kind.TRIPLE | Kind.QUAD:
            for _, group in groupby(bot_hand, key=lambda c: c.rank_index):
                cards_by_rank = list(group)
                for multi in list(combinations(cards_by_rank, len(current_pile))):
                    if beats(multi, current_pile):
                        return list(multi)
        case Kind.RUN:
            print("Not implemented")
            return None
        case _:
            return None
    return None
        

def choose_play(bot_hand: Hand, current_pile: Hand) -> Iterable[Card] | None:
    if current_pile:
        return find_lowest_beat(bot_hand, current_pile)
        # pick lowest beat
    elif bot_hand:
        # play lowest single
        return [bot_hand[0]]
    else:
        return None
    
