import random
import os

def create_deck() -> list:
    print('available_deck')
    ten_value_cards = ['J','Q','K']
    suits = ['H','C','D','S']
    deck = []
    for suit in suits:
        for i in range(9):
            deck.append(f'{suit}-{str(i+2)}')
        for card in ten_value_cards:
            deck.append(f'{suit}-{card}')
        deck.append(f'{suit}-{'A'}')   
    random.shuffle(deck)
    return deck

def strip_hand(base_hand) -> list:
    clean_hand = []
    for card in base_hand:
        discarded_suit, value = card.split('-')
        clean_hand.append(value)
    return clean_hand

def calculate_hand(base_hand) -> int:
    clean_hand = strip_hand(base_hand)
    number_of_aces = 0
    normal_card_sum = 0
    sum = 0
    # Checks to see the value of a card and totals it (unless it is an ace)
    for card in clean_hand:
        if card == 'A':
            number_of_aces += 1
        else:
            normal_card_sum = normal_card_sum + card_value(card)

    '''# debug, remove eventually
    print(f'{normal_card_sum} & {number_of_aces}')'''

    # Calculates if the total with aces is more than 21, 
    if normal_card_sum + number_of_aces + 10 <= 21 and number_of_aces > 0:
        return normal_card_sum + number_of_aces + 10
    else:
        return normal_card_sum + number_of_aces

def card_value(card) -> int:
    # sets the value of individual cards.
    if card in ['J','Q','K']:
        return 10
    elif card == 'A':
        return 11
    else: 
        return int(card)

def check_naturals(hand) -> bool:
    # Checks after the initial deal to see if any cards are natural
    hand = strip_hand(hand)
    if card_value(hand[0]) + card_value(hand[1]) == 21:
        return True
    else:
        return False

def resolve_naturals(players_hand, dealers_hand) -> bool:
    player_has_natural = check_naturals(players_hand)
    dealer_has_natural = check_naturals(dealers_hand)
    
    # Checks if there is a natural, if there is returns True.
    if player_has_natural and dealer_has_natural:
        print(f'It\'s a Tie!')
        return True
    elif dealer_has_natural:
        print(f'Dealer Wins! {dealers_hand}')
        return True
    elif player_has_natural:
        print(f'Player Wins!')
        return True
    return False

deck = create_deck()

def play():
    os.system('cls')
    global deck
    players_hand = []
    dealers_hand = []

    # Deal the initial hand to each person.
    dealers_hand.append(deck.pop())
    players_hand.append(deck.pop())
    dealers_hand.append(deck.pop())
    players_hand.append(deck.pop())
    
    print(f'The Dealers First Card is always hidden!\n\nDealer: {dealers_hand[1:]} - Score: {calculate_hand(dealers_hand)}')    
    print(f'Player: {players_hand} - Score: {calculate_hand(players_hand)}\n')

    if not resolve_naturals(players_hand, dealers_hand):
        player_turn = input('Hit or Stand? ')
        match player_turn.lower():
            case 'hit':
                os.system('cls')
                players_hand.append(deck.pop())
                print(players_hand)
            case 'stand':
                print('YOU HAVE NO LEGS JOHNNY!')
            case _:
                print('Invalid Command!')
    else:
        print('BYE!')

play()