import pygame
import sys
from card import Card
from cardrender import CardRenderer
from constants import (SCREEN_HEIGHT, SCREEN_WIDTH, CARD_W, CARD_H)

from logger import (log_state, log_event)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    gap = 10
    screen_rect = screen.get_rect()

    temp0 = CardRenderer(CARD_W,CARD_H)
    
    test_card_right = Card("Ace","Spades")
    right_card_surface = temp0.render(test_card_right)
    right_card_rect = right_card_surface.get_rect(midleft=(screen_rect.centerx + gap, screen_rect.centery))
    
    test_card_left = Card("Queen","Hearts")
    left_card_surface = temp0.render(test_card_left)
    left_card_rect = left_card_surface.get_rect(midright=(screen_rect.centerx - gap, screen_rect.centery))
    
    clock = pygame.time.Clock()
    dt = 0.0

    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # Game Loop
    while True:
        log_state() 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((20, 80, 50))
        
        screen.blit(left_card_surface, left_card_rect)
        screen.blit(right_card_surface, right_card_rect)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()
