import random
import os

current_game_deck = []
discarded_game_deck = []
players_hand = []
dealers_hand = []
suits = ['H','S','C','D']
cards = ['A', 'J', 'Q', 'K']    
running = True
game_state = 'running'
previous_round_message = ''
player_cards_dealt = 0
dealer_cards_dealt = 0
stand_or_hit = ''

def run_game():
    global current_game_deck, running
    current_game_deck = available_deck()
    while running == True:
        if game_state == 'running':
            initial_deal()
        elif game_state == 'blackjack!':
            clear_hands()
        elif game_state == 'busted':
            clear_hands()

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
    initial_deal()
    game_state == 'running'

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
        blackjack()
        deal_cards_to_player()


def blackjack() -> str: # CONVERT THIS INTO A BLACKJACK DETECTOR
    global dealers_hand, running, game_state, previous_round_message
    previous_round_state = 'First Round'
        # Deals a card to player and removes it from the deck.
    if hand_value(dealers_hand) == 21 and hand_value(players_hand) == 21:
        previous_round_message = ('TIE')
        previous_round_state = 'Tie'
        clear_hands()
    elif hand_value(dealers_hand) == 21:
        previous_round_message = (f'Dealer Wins! {dealers_hand}')
        previous_round_state = 'dealer win'
        clear_hands()
    elif hand_value(players_hand) == 21:
        previous_round_message = (f'Blackjack! Player wins!')
        previous_round_state = 'blackjack'
    elif hand_value(players_hand) > 21:
        previous_round_message = (f'Busted with {hand_value(players_hand)-21} Over! \n{players_hand}')
        previous_round_state = 'busted'
        clear_hands()
        # print(f'Your hand has {hand_value(players_hand)} points: {players_hand}')
    return previous_round_state

def deal_cards_to_player():
    global current_game_deck, players_hand, running, player_cards_dealt, stand_or_hit
    # os.system('cls')
    print(f'{game_state} - {previous_round_message}\nThe Dealer\'s first card is always hidden!\n-------------------------------\n')
    if blackjack() != 'blackjack' and blackjack() != 'busted':
        print(f'Dealer\'s Hand: {hand_value(dealers_hand[1:])} - {dealers_hand[1:]}\nPlayer\'s Hand: {hand_value(players_hand)} - {players_hand}\n')
        #print(f'Your hand has {hand_value(players_hand)} points: {players_hand}')
        stand_or_hit = input('Hit or Stand? ')
        if stand_or_hit.lower() == 'hit':
            players_hand.append(random.choice(current_game_deck))
            for card in players_hand:
                if card in current_game_deck:
                    current_game_deck.remove(card)
        elif stand_or_hit.lower() == 'stand':
            'PASSED STAND'
        deal_cards_to_dealer()

def hand_value(cards_total):
    sum = 0
    global cards, game_state
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
"""    if sum == 21:
        result = f\'{sum} - Blackjack!\'
        game_state = \'blackjack\'
    elif sum > 21:
        result = f\'Busted with {sum-21} Over!\'
        game_state = \'busted\'
    else: 
        result = f\'Your hand has {sum} points\'
""" 


def deal_cards_to_dealer():
    global dealers_hand, dealer_cards_dealt
    print(f'Dealer test passed')

run_game()