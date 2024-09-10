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
FACE_CARDS = ['A','J','Q','K']
VALUES = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
current_game_deck = []
player_hand = []
dealer_hand = []
dealt_hand = 0

def run_game():
    global current_game_deck
    current_game_deck = shuffle_cards()
    while (True):
        if dealt_hand >= 2:
            print(dealer_hand)
            break
        else:
            deal_cards()
            if dealt_hand == 2:
                return print('BlackJack!') if has_blackjack(player_hand[0],player_hand[1]) == True else print('Not BlackJack.')
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
    global current_game_deck, dealt_hand, dealer_hand, player_hand
    if dealt_hand < 2:
        # deal a random card to the dealer and remove it from the list.
        dealer_hand.append(random.choice(current_game_deck))
        for card in dealer_hand:
            if card in current_game_deck:
                current_game_deck.remove(card)
        print(f'Dealer {dealer_hand}')

        # deal a random card to the player and remove it from the list.
        player_hand.append(random.choice(current_game_deck))
        for card in player_hand:
            if card in current_game_deck:
                current_game_deck.remove(card)
        print(f'Player {player_hand}')
    dealt_hand+=1
    pass

def has_blackjack(card_1, card_2):
    global FACE_CARDS
    card_1 = card_1[2:4]
    card_2 = card_2[2:4]

    if card_1 == 'A':
        card_1 = int(11)
    elif card_1 in FACE_CARDS: 
        card_1 = int(10)            
    else:
        card_1 = card_1
    print(f'test 1 {card_1}')

    if card_2 == 'A':
        card_2 = int(11)
    elif card_2 in FACE_CARDS: 
        card_2 = int(10)            
    else:
        card_1 = card_1
    print(f'test 2 {card_2}')

    if int(card_1) + int(card_2) == 21:
        return True

def ace_value(total_value):
    
    pass

def hand_value():
    pass

def dealer_value():
    pass

def compare_hands():
    pass
run_game()