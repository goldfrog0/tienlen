import pygame
import sys
from card import Card
from cardrender import CardRenderer
from deck import Deck
from constants import (SCREEN_HEIGHT, SCREEN_WIDTH, CARD_W, CARD_H)
from hand import (Hand)

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
    player_hand = Hand(card_piles[0][0:4])

    #drawing hands
    max_width = 990
    max_step = 160
    def layout_player():
        return player_hand.layout((CARD_W,CARD_H),
                                           max_width,
                                           max_step,
                                           screen_rect.centerx,
                                           SCREEN_HEIGHT - 20)
    player_hand_rects = layout_player()

    # game running basics
    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #tracks selected cards
    selected_cards = set()

    #card lift
    selected_card_lift = 25
    
    # Game Loop
    while True:
        log_state() 
        
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    return
                case pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for card, area in reversed(player_hand_rects):
                            if card in selected_cards:
                                if area.move(0,-selected_card_lift).collidepoint(event.pos):
                                    selected_cards.remove(card) 
                                    print(f"removed: {card}")
                                    break
                            else:
                                if area.collidepoint(event.pos):     
                                    selected_cards.add(card)
                                    print(f"selected: {card}")
                                    break
                            for card in selected_cards:
                                 print(card)
                case pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN: 
                        player_hand = player_hand.without(selected_cards)
                        selected_cards = set()
                        player_hand_rects = layout_player()
                    
        screen.fill((20, 80, 50))
        
        #screen.blit(left_card_surface, left_card_rect)
        #screen.blit(right_card_surface, right_card_rect)

        for card, rect in player_hand_rects:
            if card in selected_cards:
                screen.blit(faces[card], rect.move(0, -selected_card_lift))
            else:
                screen.blit(faces[card], rect)
            
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()
