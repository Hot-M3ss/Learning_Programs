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
player_hand_suites = []
player_hand_values = []
dealer_hand = []
dealt_hand = 0
playing_blackjack = False

def run_game():
    global current_game_deck, playing_blackjack
    current_game_deck = shuffle_cards()

    # This controls if the player is on the menu or in the game.
    if playing_blackjack == False:
        play_game = input('Start Game - Y/N?: ')
        if play_game == 'Y':
            playing_blackjack = True

    # The main game logic.
    while playing_blackjack == (True):
        if dealt_hand >= 3:
            #print(f'DH: 1st Card(hidden), {dealer_hand[1:]}')
            break
        else:
            deal_cards()
            if dealt_hand == 2:
                suite_to_values(player_hand_suites)
            #print(f'{player_hand_values}, {player_hand_suites}')

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
    global current_game_deck, dealt_hand, dealer_hand, player_hand_suites
    if dealt_hand < 2:
        # deal a random card to the dealer and remove it from the list.
        dealer_hand.append(random.choice(current_game_deck))
        for card in dealer_hand:
            if card in current_game_deck:
                current_game_deck.remove(card)
        #print(f'Dealer {dealer_hand}')

        # deal a random card to the player and remove it from the list.
        player_hand_suites.append(random.choice(current_game_deck))
        for card in player_hand_suites:
            if card in current_game_deck:
                current_game_deck.remove(card)
        print(f'Player {player_hand_values}')
    elif dealt_hand >= 2:
        print('temp')
        dealt_hand+=1
    dealt_hand+=1
    pass

def suite_to_values(card):
    global FACE_CARDS, player_hand_values
    for x in card:
        if x[2:4] in FACE_CARDS and not 'A': 
            player_hand_values.append(int(10))
        elif x[2:4] not in FACE_CARDS:
            player_hand_values.append(int(x[2:4]))
        if x[2:4] == 'A': 
            player_hand_values.append('A')
    has_blackjack(player_hand_values)
    ace_value(player_hand_values)

def has_blackjack(bj_values):

    pass

def ace_value(cards):
    sum = 0
    temp_values = []
    for x in cards:
        if x != 'A':
            temp_values.append(x)
    for n in temp_values:
        sum = sum + n
    if sum > 10 and x == 'A':
        temp_values.append(1)
    else: temp_values.append(11)
    print(f'{temp_values} and sum {sum}')

def compare_hands():
    pass

run_game()