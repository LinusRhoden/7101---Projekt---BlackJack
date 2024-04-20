import random 
import time 

bank = int(input("Buy in amount?"))

deck = []
ranks = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
suits = ["spades", "hearts", "clubs", "diamonds"]

for suit in suits:
    for rank in ranks:
        deck.append([suit, rank])

def shuffle():
    random.shuffle(deck)

def deal(number):
    cards = []
    for i in range(number):
      card = deck.pop()
      cards.append(card)
    return cards

def value_f(x):
    value = 0
    if x == "A":
       value = 11
    elif x == "K" or x == "Q" or x =="J":
       value = 10
    else:
       value = x
    return value

def bust(value):
    if value > 21:
        print("Bust!")
        
def hit(the_hand, value):
    h_card = deck.pop()
    the_hand.append(h_card)
    print(the_hand)
    value = value + value_f(the_hand[-1][1])
    print(value)
    bust(value)
    return value

def win(bank, bet):
    if t_value == 21 and d_value != 21:
        bank = bank + bet * 1.5
        print("Player won with BJ!")
        print("You won", bet * 1.5)
    elif t_value > d_value and t_value < 22 or d_value > 21:
        bank = bank + bet 
        print("Player won!")
        print("You won", bet * 2)
    elif d_value > t_value and d_value < 22 or t_value > 21:
        bank = bank - bet 
        print("Dealer won!")
    else:
        print("Push!")
    print(bank)
    return bank

while bank > 0:
    bet = int(input("Bet?"))
    if bet > bank:
        print("Not enough bankZ")
        bet = int(input("Bet?"))
    shuffle()
    hand = deal(2)
    hand_2 = deal(2)
    print("Player's hand")
    print(hand[0])
    print(value_f(hand[0][1]))
    print("Dealer's hand")
    print(hand_2[0])
    d_value = (value_f(hand_2[0][1])) + value_f(hand_2[1][1])
    print(value_f(hand_2[0][1]))
    print("Player's hand")
    print(hand[0], hand[1])
    t_value = (value_f(hand[0][1])) + (value_f(hand[1][1]))
    print(t_value)

    hos = input("hit or stand?")
    while hos == "h":
        t_value = hit(hand, t_value)
        if t_value > 21:
            hos = "s"
        else:
            hos = input("hit or stand?")

    print(hand_2)
    print(d_value)
    while d_value < 17 and t_value < 22:
        d_value = hit(hand_2, d_value)

    bank = win(bank, bet)