#!/usr/bin/env python
import pygame

class RectangleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.LayeredUpdates, ...]

    def __init__(self, x: float, y: float, height: float, width: float) -> None:
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.height = height
        self.width = width

    def collides_with(self, other):
        pass

    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pass

    def update(self, dt: float) -> None:
        # must overide
        pass
