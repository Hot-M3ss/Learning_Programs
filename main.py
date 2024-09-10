# BlackJack

''' 
import random
deck = []
suits = ["H", "S", "C", "D"]
cards = ["A", "J", "Q", "K"]
for x in range(9):
    cards.append(str(x + 2))
for suit in suits:
    for card in cards:
        deck.append(suit + "-" + card)
print(len(deck))
live_deck = deck
random.shuffle(live_deck)
print(live_deck[0:4])
'''
import random

VALUES = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
current_game_deck = []
def run_game():
    global current_game_deck
    current_game_deck = shuffle_cards()
    while (True):
        deal_cards()
        if 0 == 1:
            break

def available_deck():
    hearts = []
    diamonds = []
    clubs = []
    spades = []
    for i in VALUES: 
        hearts.append('H-'+i)
        diamonds.append('D-'+i)
        clubs.append('C-'+i)
        spades.append('S-'+i)
    deck = hearts+diamonds+clubs+spades
    return deck

def shuffle_cards():
    my_deck = available_deck()
    random.shuffle(my_deck)
    return my_deck

def deal_cards():
    global current_game_deck
    player_hand = []
    dealer_hand = []
    print(current_game_deck)
    player_hand = random.choice(current_game_deck)
    current_game_deck.remove(player_hand)

def has_blackjack(card_1, card_2):
    pass

def ace_value():
    pass

def hand_value():
    pass

def dealer_value():
    pass

def compare_hands():
    pass
run_game()