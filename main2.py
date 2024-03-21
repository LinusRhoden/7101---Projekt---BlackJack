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



shuffle()


hand = deal(2)
print(hand)
print(hand[0][2])