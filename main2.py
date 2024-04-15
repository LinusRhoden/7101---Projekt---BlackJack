import random 
import time 

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

def value_f(x):
    value = 0
    if x == "A":
       value = 11
    elif x == "K" or x == "Q" or x =="J":
       value = 10
    else:
       value = x
    return value



shuffle()


hand = deal(2)
p_value = (value_f(hand[0][1])) + (value_f(hand[1][1]))
print(p_value)