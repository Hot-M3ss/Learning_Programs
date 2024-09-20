import random
import os

current_game_deck = []
players_hand = []
dealers_hand = []
suits = ['H','S','C','D']
cards = ['A', 'J', 'Q', 'K']    
running = True
has_stood = False
player_cards_dealt = 0
dealer_cards_dealt = 0

def run_game():
    print('run_game')
    global current_game_deck, running
    current_game_deck = available_deck()
    # os.system('cls')
    while running == True:
        continue_game()
    exit()

def available_deck():
    print('available_deck')
    global suits, cards
    deck = []
    for suit in suits:
        for i in range(9):
            deck.append(f'{suit}-{str(i+2)}')
        for card in cards:
            deck.append(f'{suit}-{card}')        
    random.shuffle(deck)
    return deck

def continue_game():
    print('continue_game')
    global running
    # Asks for and validates the players action
    continue_input = input('Continue: Yes or No? ')
    match continue_input.lower():
        case 'yes':
            # os.system('cls')
            continue_game()
        case 'no':
            # os.system('cls')
            print('Thank you for playing!')
            running = False
        case _:
            print('Not a valid command!')
            continue_game()

def clear_hands():
    print('clear_hands')
    global players_hand, dealers_hand, player_cards_dealt, dealer_cards_dealt, running
    # Clears all cards from the players hands
    if player_cards_dealt > 0:
        players_hand.clear()
        player_cards_dealt = 0

    # Clears all cards from the dealers hand
    if dealer_cards_dealt > 0:
        dealers_hand.clear()
        dealer_cards_dealt = 0
    
def initial_deal():
    print('initial_deal')
    global current_game_deck, dealers_hand, players_hand
    # Deals the first two cards to both the player and dealer.
    dealers_hand.append(current_game_deck.pop())
    players_hand.append(current_game_deck.pop())
    dealers_hand.append(current_game_deck.pop())
    players_hand.append(current_game_deck.pop())
    outcome_check()

def outcome_check(): # CONVERT THIS INTO A BLACKJACK DETECTOR
    print('outcome_check')
    global dealers_hand, players_hand
    print(f'The Dealer\'s first card is always hidden!\n\nDealer\'s Hand: {hand_value(dealers_hand[1:])} - {dealers_hand[1:]}\nPlayer\'s Hand: {hand_value(players_hand)} - {players_hand}\n')
    # Test win and lose conditions
    if hand_value(dealers_hand) == 21 and hand_value(players_hand) == 21:
        print(f'Hidden Card: {dealers_hand[0]} - it\'s a Tie!\n')
        clear_hands()
    elif hand_value(dealers_hand) == 21:
        print(f'Hidden Card: {dealers_hand[0]} - Dealer Wins!\n')
        clear_hands()
    elif hand_value(players_hand) == 21:
        print(f'Hidden Card: {dealers_hand[0]} - Blackjack! Player wins!\n')
        clear_hands()
    elif hand_value(players_hand) > 21:
        print(f'Hidden Card: {dealers_hand[0]} - Busted with {hand_value(players_hand)-21} Over!\n')
        clear_hands()
    else:
        hit_stand()
    
def deal_card(deck):
    return deck.pop()

def hit_stand():
    print('hit_stand')
    global has_stood
    # Asks for and validates the players action
    hit_or_stand_input = input('Hit or Stand? ')
    match hit_or_stand_input.lower():
        case 'hit':
            # os.system('cls')
            players_hand.append(deal_card(current_game_deck))
            print(players_hand)
            # os.system('cls')
            has_stood = True
            # deal_cards_to_dealer()
        case _:
            print('Not a valid Command!')
            hit_stand()

def deal_cards_to_player():
    global current_game_deck, players_hand
    # Deals a card to a player if called.
    players_hand.append(random.choice(current_game_deck))
    current_game_deck.remove(players_hand[-1])
    outcome_check()

'''def deal_cards_to_dealer():
    global dealers_hand, dealer_cards_dealt, current_game_deck
    if has_stood == True:
        if hand_value(dealers_hand) <= 16:
            dealers_hand.append(random.choice(current_game_deck))
            current_game_deck.remove(players_hand[-1])
            dealer_cards_dealt += 1
            deal_cards_to_dealer()

        elif hand_value(dealers_hand) == 17:
            if ('H-A' or 'S-A' or 'C-A' or 'D-A') in dealers_hand:
                print("soft 17")

        elif hand_value(dealers_hand) > 17:
            outcome_check()
            print('sucess')
    has_stood == False
'''

def hand_value(cards_total):
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