#!/usr/bin/env python

from card import(Card)
from collections.abc import Sequence
import random

class Hand(Sequence[Card]):
    def __init__(self, cards: list[Card] ) -> None:
        self._cards = sorted(cards)

    def __getitem__(self, key):
        return self._cards[key]

    def __len__(self):
        return len(self._cards)

    def __str__(self) -> str:
        card_list = []
        for card in self._cards:
            card_list.append(str(card))
        return "\n".join(card_list)
