import random

current_game_deck = []
players_hand = []
dealers_hand = []
suits = ['H','S','C','D']
cards = ['A', 'J', 'Q', 'K']    
running = True
game_state = 'running'
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
            running = False
            clear_hands()
        elif game_state == 'busted':
            running = False
            clear_hands()

def clear_hands():
    global players_hand, dealers_hand, player_cards_dealt, dealer_cards_dealt, running
    # Clears all cards from the players hands
    for x in players_hand:
        players_hand.remove(x)
    player_cards_dealt = 0
    # Clears all cards from the dealers hand
    for x in dealers_hand:
        dealers_hand.remove(x)
    dealer_cards_dealt = 0
    running = False

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
        print(dealers_hand)

    # deal the initial cards to the player
    if player_cards_dealt >= 2:
        deal_cards_to_player()
        blackjack()
        #print(f'{hand_value(players_hand)} - {players_hand}')
    else:
        players_hand.append(random.choice(current_game_deck))
        for card in players_hand:
            if card in current_game_deck:
                current_game_deck.remove(card)
        player_cards_dealt += 1
        

def blackjack(): # CONVERT THIS INTO A BLACKJACK DETECTOR
    global dealers_hand, running, game_state
        # Deals a card to player and removes it from the deck.
    if hand_value(dealers_hand) == 21 and hand_value(players_hand) == 21:
        print (f'TIE')
        clear_hands()
    elif hand_value(dealers_hand) == 21:
        print (f'Dealer Wins!')
        clear_hands()
    elif hand_value(players_hand) == 21:
        print(f'Blackjack! Player wins!')
        game_state = 'blackjack'

    elif hand_value(players_hand) > 21:
        print(f'Busted with {hand_value(players_hand)-21} Over!\n{players_hand}')
        game_state = 'busted'
    else:
        hand_value(players_hand)
        

def deal_cards_to_player():
    global current_game_deck, players_hand, running, player_cards_dealt, stand_or_hit    
    if blackjack() != 'Blackjack!':
        print(f'Your hand has {hand_value(players_hand)} points: {players_hand}')
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
    print(f'Dealers Hand, First Hidden: {dealers_hand[1:]}')
    print(f'Dealer test passed')

run_game()