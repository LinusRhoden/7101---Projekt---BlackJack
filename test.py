import pygame
import random
import time
import os

pygame.init()

WIDTH,HEIGHT = 800,600
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("BlackJack")


GREEN = (0,50,0)

FPS = 60

DECK_IMAGE = pygame.image.load('resources/cards/cardback.png')
card_images = {}
card_images["spadeK"] = pygame.image.load('resources/cards/ks.png')
card_images["heartK"] = pygame.image.load('resources/cards/kh.png')
card_images["clubK"] = pygame.image.load('resources/cards/kc.png')
card_images["diamondK"] = pygame.image.load('resources/cards/kd.png')
card_images["spadeQ"] = pygame.image.load('resources/cards/qs.png')
card_images["heartQ"] = pygame.image.load('resources/cards/qh.png')
card_images["clubQ"] = pygame.image.load('resources/cards/qc.png')
card_images["diamondQ"] = pygame.image.load('resources/cards/qd.png')
card_images["diamondA"] = pygame.image.load('resources/cards/ad.png')
card_images["clubA"] = pygame.image.load('resources/cards/ac.png')
card_images["heartA"] =pygame.image.load('resources/cards/ah.png')
card_images["spadeA"] = pygame.image.load('resources/cards/as.png')
card_images["diamond2"] =pygame.image.load('resources/cards/2d.png')
card_images["club2"] = pygame.image.load('resources/cards/2c.png')
card_images["heart2"] = pygame.image.load('resources/cards/2h.png')
card_images["spade2"] = pygame.image.load('resources/cards/2s.png')
card_images["diamond3"] = pygame.image.load('resources/cards/3d.png')
card_images["club3"] = pygame.image.load('resources/cards/3c.png')
card_images["heart3"] = pygame.image.load('resources/cards/3h.png')
card_images["spade3"] = pygame.image.load('resources/cards/3s.png')
card_images["diamond4"] = pygame.image.load('resources/cards/4d.png')
card_images["club4"] = pygame.image.load('resources/cards/4c.png')
card_images["heart4"] = pygame.image.load('resources/cards/4h.png')
card_images["spade4"] = pygame.image.load('resources/cards/4s.png')
card_images["diamond5"] = pygame.image.load('resources/cards/5d.png')
card_images["club5"] = pygame.image.load('resources/cards/5c.png')
card_images["heart5"] = pygame.image.load('resources/cards/5h.png')
card_images["spade5"] = pygame.image.load('resources/cards/5s.png')
card_images["diamond6"] = pygame.image.load('resources/cards/6d.png')
card_images["club6"] = pygame.image.load('resources/cards/6c.png')
card_images["heart6"] = pygame.image.load('resources/cards/6h.png')
card_images["spade6"] = pygame.image.load('resources/cards/6s.png')
card_images["diamond7"] = pygame.image.load('resources/cards/7d.png')
card_images["club7"] = pygame.image.load('resources/cards/7c.png')
card_images["heart7"] = pygame.image.load('resources/cards/7h.png')
card_images["spade7"] = pygame.image.load('resources/cards/7s.png')
card_images["diamond8"] = pygame.image.load('resources/cards/8d.png')
card_images["club8"] = pygame.image.load('resources/cards/8c.png')
card_images["heart8"] = pygame.image.load('resources/cards/8h.png')
card_images["spade8"] = pygame.image.load('resources/cards/8s.png')
card_images["diamond9"] = pygame.image.load('resources/cards/9d.png')
card_images["club9"] = pygame.image.load('resources/cards/9c.png')
card_images["heart9"] = pygame.image.load('resources/cards/9h.png')
card_images["spade9"] = pygame.image.load('resources/cards/9s.png')
card_images["diamond10"] = pygame.image.load('resources/cards/10d.png')
card_images["club10"] = pygame.image.load('resources/cards/10c.png')
card_images["heart10"] = pygame.image.load('resources/cards/10h.png')
card_images["spade10"] = pygame.image.load('resources/cards/10s.png')
card_images["diamondJ"] = pygame.image.load('resources/cards/jd.png')
card_images["clubJ"] = pygame.image.load('resources/cards/jc.png')
card_images["heartJ"] = pygame.image.load('resources/cards/jh.png')
card_images["spadeJ"] = pygame.image.load('resources/cards/js.png')


def draw_screen():
    SCREEN.fill(GREEN)
    SCREEN.blit(DECK_IMAGE,(350,-50))
    pygame.display.update()
   
deck = []
ranks = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
suits = ["spade", "heart", "club", "diamond"]

for suit in suits:
    for rank in ranks:
        card_file_name = suit + str(rank) 
        deck.append([suit, rank, card_file_name])

print(deck)
def shuffle():
    random.shuffle(deck)

def deal(number):
    cards = []
    for i in range(number):
      card = deck.pop()
      cards.append(card)
    return cards

def main():
    clock = pygame.time.Clock()
    run =True
    while run:
        clock.tick(FPS)
        
     

        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                run = False

    pygame.QUIT()





draw_screen()

main()



