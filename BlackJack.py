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
            print(f'Blackjack!')
            running = False
            clear_hands()
        else:
            print(f'Busted')
            running = False
            clear_hands()

        ''
       # if player_cards_dealt == 2:
        #    running = False
def clear_hands():
    global players_hand, dealers_hand, player_cards_dealt, dealer_cards_dealt
    # Clears all cards from the players hands
    for x in players_hand:
        players_hand.remove(x)
    player_cards_dealt = 0
    # Clears all cards from the dealers hand
    for x in dealers_hand:
        dealers_hand.remove(x)
    dealer_cards_dealt = 0
    pass
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
    if dealer_cards_dealt >= 2:
        deal_cards_to_dealer()
    else:
        dealers_hand.append(random.choice(current_game_deck))
        for card in dealers_hand:
            if card in current_game_deck:
                current_game_deck.remove(card)
        dealer_cards_dealt += 1
        print(dealers_hand)

    # deal the initial cards to the player
    if player_cards_dealt >= 2:
        deal_cards_to_player()
        print(f'{hand_value(players_hand)} - {players_hand}')
    else:
        players_hand.append(random.choice(current_game_deck))
        for card in players_hand:
            if card in current_game_deck:
                current_game_deck.remove(card)
        player_cards_dealt += 1
        hand_value(players_hand)
        print(f'{hand_value(players_hand)} - {players_hand}')
    pass

def deal_cards_to_player():
    global current_game_deck, players_hand, running, player_cards_dealt, stand_or_hit
    # Deals a card to player and removes it from the deck.
    if hand_value(players_hand) != 'Blackjack!':
        stand_or_hit = input('Hit or Stand? ')
        if stand_or_hit.lower() == 'hit':
            players_hand.append(random.choice(current_game_deck))
            for card in players_hand:
                if card in current_game_deck:
                    current_game_deck.remove(card)
        elif stand_or_hit.lower() == 'stand':
            'PASSED STAND'
            deal_cards_to_dealer()
            running = False

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
    if sum == 21:
        result = f'{sum} - Blackjack!'
        game_state = 'blackjack'
    elif sum > 21:
        result = f'Busted with {sum-21} Over!'
        game_state = 'busted'
    else: 
        result = f'Your hand has {sum} points'
    return result

def deal_cards_to_dealer():
    print(f'Dealer test passed')
    pass

run_game()