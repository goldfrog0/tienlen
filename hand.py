#!/usr/bin/env python

from card import(Card)
from collections.abc import (Sequence)
from typing import (Iterable)
import pygame

class Hand(Sequence[Card]):
    def __init__(self, cards: Iterable[Card] ) -> None:
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

    def layout(self,
               card_size: tuple[int, int],
               max_width: int,
               max_step: int,
               center_x: int,
               bottom: int
               ) -> list[tuple[Card, pygame.Rect]]:
        width, height = card_size

        if len(self) > 1:
            step = min(max_step, (max_width - width) // (len(self) - 1))
        else:
            step = max_step
        fan_width = width + (len(self) - 1)*step
        left_edge = center_x - (fan_width // 2)
        player_hand_rects = []
        for idx, card in enumerate(self._cards):
            x = left_edge + idx * step
            rect = pygame.Rect(0, 0, width, height)
            rect.bottomleft = (x, bottom)
            player_hand_rects.append((card, rect))
        return player_hand_rects

    def without(self, removed_cards: set[Card]):
        new_hand_list = []
        for card in self:
            if card not in removed_cards:
                new_hand_list.append(card)
            if card in removed_cards:
                pass
        return Hand(new_hand_list)
