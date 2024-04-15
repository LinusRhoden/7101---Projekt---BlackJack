import pygame
import random
import time
import os
import sys

pygame.init()

#Set default values
WIDTH,HEIGHT = 800,600
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("BlackJack")

text_font =  pygame.font.SysFont(None, 30)

#Function to print text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    SCREEN.blit(img, (x, y))


def draw_screen():
    SCREEN.fill(GREEN)
    draw_text("", text_font, (255, 255, 255), 270, 30)    
    draw_text("", text_font, (255, 255, 255), 600, 270)  
    pygame.display.update()

GREEN = (0,50,0)

FPS = 60

DECK_IMAGE = pygame.image.load('resources/cards/cardback.png')
card_images = {}
#Load every card in a dict
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


deck = []
ranks = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
suits = ["spade", "heart", "club", "diamond"]

#Create all cards
for suit in suits:
    for rank in ranks:
        card_file_name = suit + str(rank) 
        deck.append([suit, rank, card_file_name])

print(deck)
def shuffle():
    random.shuffle(deck)

#Deal x amount of cards
def deal(number):
    cards = []
    for i in range(number):
      card = deck.pop()
      cards.append(card)
    return cards

#Return a value to a hand 
def value_f(x):
    value = 0
    if x == "A":
       value = 11
    elif x == "K" or x == "Q" or x =="J":
       value = 10
    else:
       value = x
    return value

#Create a font object
font = pygame.font.Font(None, 24)

#Create a surface for the button
button_surface = pygame.Surface((150, 50))

# Render text on the button
text = font.render("Hit", True, (0, 0, 0))
text_rect = text.get_rect(center=(button_surface.get_width()/2, button_surface.get_height()/2))

# Create a pygame.Rect object 
button_rect = pygame.Rect(125, 125, 150, 50)



def main():
    hand = deal(2)
    d_hand = deal(2)
    clock = pygame.time.Clock()
    run =True
    p_value = 0
    d_value = 0 
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                run = False
            # Check for the mouse button down event
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Call the on_mouse_button_down() function
                if button_rect.collidepoint(event.pos):
                    print("Button clicked!")  

        p_value = (value_f(hand[0][1])) + (value_f(hand[1][1]))
        d_value = (value_f(d_hand[0][1]))
        SCREEN.blit(card_images[hand[0][2]],(330, 350)) 
        SCREEN.blit(card_images[hand[1][2]],(360, 340))  
        SCREEN.blit(card_images[d_hand[0][2]],(270, 70)) 
        SCREEN.blit(DECK_IMAGE,(380, 70))  
        draw_text(str(p_value), text_font, (255, 255, 255), 490, 475)  
        draw_text(str(d_value), text_font, (255, 255, 255), 490, 190)  
        pygame.display.update() 
        
        # Check if the mouse is over the button. This will create the button hover effect
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(button_surface, (127, 255, 212), (1, 1, 148, 48))
        else:
            pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
            pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
            pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
            pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)

        # Shwo the button text
        button_surface.blit(text, text_rect)

        # Draw the button on the screen
        SCREEN.blit(button_surface, (button_rect.x, button_rect.y))
    



    pygame.QUIT()
    sys.exit()





draw_screen()

shuffle()

main()
