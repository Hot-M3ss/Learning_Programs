import os
import random

def create_deck() -> list:
    ten_value_cards = ['J','Q','K']
    suits = ['H','C','D','S']
    deck = []
    # Assigns each card to a suit in order: Ace, Numbers, and Face Cards
    for suit in suits:
        deck.append(f'{suit}-A')
        for number in range(9):
            deck.append(f'{suit}-{str(number+2)}')
        for face in ten_value_cards:
            deck.append(f'{suit}-{face}')
    random.shuffle(deck)
    return deck

def deal_card(hand: list):
    hand.append(globalVariables['deck'].pop())

def print_hand() -> None:
    print(f'{players_hand}')

def players_turn(players_hand):
    players_input = input('Would you like to hit or stand? ').lower()
    match players_input:
        case 'hit':
            deal_card(players_hand)
            print_hand(players_hand)
        case 'stand':
            pass
        case _:
            pass

globalVariables = {
    'deck':create_deck(),
    'dealers_hand': [],
    'players_hand': []
}


def play():
    # init variables
    global globalVariables
    # Runs the cls to clear the terminal
    os.system('cls')
    # The main game logic.
    while(True):
        # Checks to make sure the deck is not too small.
        if len(globalVariables['deck']) < 10:
            globalVariables['deck'] = create_deck()
            break

        deal_card(globalVariables['dealers_hand'])
        deal_card(globalVariables['players_hand'])
        deal_card(globalVariables['dealers_hand'])
        deal_card(globalVariables['players_hand'])

        print(globalVariables['players_hand'], globalVariables['dealers_hand'][1:])

        players_turn(globalVariables['players_hand'])
    
        break

play()
    