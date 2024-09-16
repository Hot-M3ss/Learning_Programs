import random
import os

current_game_deck = []
players_hand = []
dealers_hand = []
suits = ['H','S','C','D']
cards = ['A', 'J', 'Q', 'K']    
running = True
player_cards_dealt = 0
dealer_cards_dealt = 0
hit_or_stand = ''

def run_game():
    global current_game_deck, running
    current_game_deck = available_deck()
    os.system('cls')
    while running == True:
        continue_game()
    exit()

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

def continue_game():
    global running
    # Asks for and validates the players action
    continue_input = input('Continue: Yes or No? ')
    if continue_input.lower() != 'yes' and continue_input.lower() != 'no':
        print('Not a valid command!')
        continue_game()
    # Checks which value was entered.
    if continue_input.lower() == 'yes':
        os.system('cls')
        initial_deal()
    elif continue_input.lower() == 'no':
        running = False

def clear_hands():
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
    global player_cards_dealt, dealer_cards_dealt, current_game_deck, dealers_hand, players_hand, running
    # deal the initial cards to the dealer
    if dealer_cards_dealt < 2:
        dealers_hand.append(random.choice(current_game_deck))
        for card in dealers_hand:
            if card in current_game_deck:
                current_game_deck.remove(card)
        dealer_cards_dealt += 1

    # deal the initial cards to the player
    if player_cards_dealt < 2:
        players_hand.append(random.choice(current_game_deck))
        for card in players_hand:
            if card in current_game_deck:
                current_game_deck.remove(card)
        player_cards_dealt += 1
        initial_deal()
    else:
        outcome_check()
        
def outcome_check(): # CONVERT THIS INTO A BLACKJACK DETECTOR
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

def hit_stand():
    # Asks for and validates the players action
    hit_or_stand_input = input('Hit or Stand? ')
    if hit_or_stand_input.lower() != 'hit' and hit_or_stand_input.lower() != 'stand':
        print('Not a valid command!')
        hit_stand()
    # Checks which value was entered.
    if hit_or_stand_input.lower() == 'hit':
        os.system('cls')
        deal_cards_to_player()
    elif hit_or_stand_input.lower() == 'stand':
        os.system('cls')
        deal_cards_to_dealer()

def deal_cards_to_player():
    global current_game_deck, players_hand
    # Deals a card to a player if called.
    players_hand.append(random.choice(current_game_deck))
    for card in players_hand:
        if card in current_game_deck:
            current_game_deck.remove(card)
    outcome_check()

def deal_cards_to_dealer():
    global dealers_hand, dealer_cards_dealt
    for x in dealers_hand:
        if hand_value(dealers_hand) <= 17 and x == 'A':
            'test'
'''test'''

def hand_value(cards_total):
    sum = 0
    for x in cards_total:
        if x[2:4] not in cards:
            sum = sum + int(x[2:4])
        elif x[2:4] in cards and x[2:4]!= 'A':
            sum = sum + 10
    for x in cards_total:
        if x[2:4] == 'A':
            if sum <= 10:
                sum = sum + 11
            else: sum = sum + 1
    return sum

run_game()