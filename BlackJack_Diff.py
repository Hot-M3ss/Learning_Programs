from os import system
import random

current_game_deck = []
suits = ['H','S','C','D']
cards = ['A', 'J', 'Q', 'K']    
running = True
has_stood = False
player_cards_dealt = 0
dealer_cards_dealt = 0

def available_deck():
    global suits, cards
    deck = []
    for suit in suits:
        for i in range(9):
            deck.append(f'{suit}-{str(i+2)}')
        for card in cards:
            deck.append(f'{suit}-{card}')        
    random.shuffle(deck)
    return deck

def run_game():
    global current_game_deck, running, dealers_hand, players_hand
    current_game_deck = available_deck()
    # os.system('cls')
    while running == True:
        players_hand = []
        dealers_hand = []
        # Initial Dealer
        dealers_hand.append(current_game_deck.pop())
        players_hand.append(current_game_deck.pop())
        dealers_hand.append(current_game_deck.pop())
        players_hand.append(current_game_deck.pop())

        if resolve_naturals(dealers_hand, players_hand):
            ''
        else:
            # Main logic to detect a bust
            # detect dealer bust and declare player win
            # detect if there is a tie between the dealer and player.
            # check if player score is higher than the dealer.
            # else declare the player a loser.
            NotImplementedError()
        exit()

def check_naturals(hand) -> bool:
    # This function checks both card
    if hand[0] + hand[1] == 21:
        return True
    else: False
    NotImplementedError('Not implemented.')
    
def resolve_naturals(dealers_hand, players_hand):
    player_has_naturals = check_naturals(players_hand)
    dealer_has_naturals = check_naturals(dealers_hand)
        # Dealer & Player Tied
    if check_naturals(dealers_hand) and check_naturals(players_hand):
        print('Tie')
    # Dealer BlackJack
    elif check_naturals(dealers_hand):
        print('dealer wins')
    # Player BlackJack
    elif check_naturals(players_hand):
        print('player wins!')

def card_value(card):
    NotImplementedError('Not implemented.')

def hand_value(cards_total): #REDO REQUIRED
    sum = 0
    # calculates the value of the hand without Aces
    for card in cards_total:
        suit, value = card.split('-')
        if value not in cards:
            sum = sum + int(value)
        elif value in ['J','Q','K']:
            sum = sum + 10
    for card in cards_total:
        suit, value = card.split('-')
        if value == 'A':
            if sum <= 10:
                sum = sum + 11
            else: sum = sum + 1
    return sum

run_game()