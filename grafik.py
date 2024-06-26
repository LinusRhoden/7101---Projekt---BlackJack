import pygame
import random
import time
import sys

pygame.init()

GREEN = (0,50,0)  
GRAY = (200, 200, 200)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WHITE_HOVER = (250, 249, 246)

mouse_down = False
p_value = 0
d_value = 0 
hand = []
d_hand = []
FPS = 60
d_stand = False
bank = 1000
bet = 0


#Set default values
WIDTH,HEIGHT = 800,600
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("BlackJack")

text_font =  pygame.font.SysFont(None, 30)

#Function to print text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    SCREEN.blit(img, (x, y))

# Function to print values
def draw_value(value, text_col, x, y):
    draw_text(str(value), text_font, text_col, x, y)  

def draw_screen():
    SCREEN.fill(GREEN)
    pygame.display.update()

#Load every card in a dict
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

#Add new cards into a hand
def hit(the_hand, value):
    global p_value, d_value
    h_card = deck.pop()
    the_hand.append(h_card)
    print(the_hand)
    if the_hand == hand:
        p_value = value + value_f(the_hand[-1][1])
    elif the_hand == d_hand: 
        d_value = value + value_f(the_hand[-1][1])
    return value

def bust(value):
    global p_value, d_value
    if value > 21:
        if value == p_value:
            draw_text("Player Bust!", text_font, (255, 255, 255), 600, 270)  
        elif value == d_value:
            draw_text("Dealer Bust!", text_font, (255, 255, 255), 600, 270)  

# Add a function to handle betting
def place_bet():
    global bank, bet
    # Implement your betting interface here
    # You can use input(), buttons, sliders, etc. to get the bet amount from the player
    bet = int(input("Enter your bet amount: "))
    while bet > bank:
        print("You don't have enough money. Your bank: ", bank)
        bet = int(input("Enter a valid bet amount: "))
    bank -= bet

def win():
    global p_value, d_value, bet, bank
    if p_value == 21 and d_value != 21:
        bank += bet * 1.5
        draw_text("Player BJ!", text_font, (255, 255, 255), 350, 275) 
    elif p_value > d_value and p_value < 22 or d_value > 21:
         bank += bet * 2
         draw_text("Player Won!", text_font, (255, 255, 255), 350, 275)   
    elif p_value < d_value and d_value < 22 or p_value > 21:
        draw_text("Dealer Won!" , text_font, (255, 255, 255), 350, 275) 
    elif p_value == d_value and p_value < 22:
        bank += bet
        draw_text("Its a Push!", text_font, (255, 255, 255), 350, 275)  
     
#Function to create buttons 
def create_button(screen, color, x, y, width, height, text, text_color):
    global mouse_down, p_value, hand, d_hand, d_value, d_stand
    pygame.draw.rect(screen, color, (x, y, width, height))

    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surface, text_rect)

    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse_pos[0] > x and y + height > mouse_pos[1] > y:
        pygame.draw.rect(screen, WHITE_HOVER, (x, y, width, height))    
        screen.blit(text_surface, text_rect)

        if click[0] == 1 and text == "Hit" and not mouse_down:
            hit(hand, p_value)
            bust(p_value)
            mouse_down = True
        
        if click[0] == 1 and text == "Stand" and not mouse_down:
            d_value = value_f(d_hand[0][1]) + value_f(d_hand[1][1]) 
            while d_value < 17:
                hit(d_hand, d_value)
                bust(d_value)
            if d_value > 16:
                d_stand = True
            mouse_down = True 
            win()

        if click[0] == 0:
            mouse_down = False



def main():
    clock = pygame.time.Clock()
    run =True
    global hand, d_hand, p_value, d_value, d_stand
    if not hand and not d_hand: # Deal the cards 
        hand = deal(2)
        d_hand = deal(2)
        p_value = (value_f(hand[0][1])) + (value_f(hand[1][1]))
        d_value = (value_f(d_hand[0][1]))

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                run = False

        # Blit all cards using a for loop
        player_card_x = 330
        player_card_y = 350
        for card in hand:
            card_image = card_images[card[2]]
            SCREEN.blit(card_image, (player_card_x, player_card_y))
            player_card_x += 20
            player_card_y -= 5
        
        SCREEN.blit(card_images[d_hand[0][2]],(270, 70)) 
        SCREEN.blit(DECK_IMAGE,(330, 70)) 
        d_card_x = 270
        d_card_y = 70
        if len(d_hand) > 2 or d_stand:
            for card in d_hand:
                card_image = card_images[card[2]]
                SCREEN.blit(card_image, (d_card_x, d_card_y))
                d_card_x += 60

        # Draw a rectangle to hide old values
        pygame.draw.rect(SCREEN, GREEN, (490, 475, 30, 30)) 
        pygame.draw.rect(SCREEN, GREEN, (490, 190, 30, 30))
        draw_value(p_value, (255, 255,255), 490, 475)
        draw_value(d_value, (255, 255, 255), 490, 190)  

        pygame.draw.rect(SCREEN, GREEN, (50, 550, 50, 50))
        draw_value(bank, (255, 255, 255), 50, 550)

        create_button(SCREEN, WHITE, 600, 200, 100, 50, "Hit", BLACK)
        create_button(SCREEN, WHITE, 600, 300, 100, 50, "Stand", BLACK)    

        pygame.display.update() 
      

    pygame.QUIT()
    sys.exit()

#place_bet()

draw_screen()

shuffle()

main()