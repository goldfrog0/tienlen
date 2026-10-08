import pygame
import sys
from card import Card
from cardrender import CardRenderer
from deck import Deck
from constants import (SCREEN_HEIGHT, SCREEN_WIDTH, CARD_W, CARD_H)

from logger import (log_state, log_event)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    gap = 10
    screen_rect = screen.get_rect()

    temp0 = CardRenderer(CARD_W,CARD_H)
    #Building new deck
    #seeded for development purposes
    originaldeck = Deck(seed=4)

    # render faces
    faces = {card: temp0.render(card) for card in originaldeck}
    originaldeck.shuffle()
    print(len(faces), faces[originaldeck[0]].get_size())
    
    card_piles = originaldeck.deal(4)
    player_hand = card_piles[0]

    card_step = 70
    fan_width = CARD_W + (len(player_hand) - 1)*card_step
    leftmost_card_edge = (SCREEN_WIDTH - fan_width) // 2
    card_bottoms = SCREEN_HEIGHT - 20

    #drawing hands
    player_hand_rects = []
    for idx, card in enumerate(player_hand):
        x = leftmost_card_edge + idx * card_step
        rect = faces[card].get_rect(bottomleft=(x, card_bottoms))
        player_hand_rects.append((card,rect))
    
    # game running basics
    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # Game Loop
    while True:
        log_state() 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((20, 80, 50))
        
        #screen.blit(left_card_surface, left_card_rect)
        #screen.blit(right_card_surface, right_card_rect)

        for card, rect in player_hand_rects:
            screen.blit(faces[card], rect)
            
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()
