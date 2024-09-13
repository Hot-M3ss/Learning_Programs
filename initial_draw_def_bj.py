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

def initial_deal():
    global player_cards_dealt, dealer_cards_dealt, current_game_deck, dealers_hand, players_hand, running
    # deal the initial cards to the dealer
    if dealer_cards_dealt < 2:
        dealers_hand.append(random.choice(current_game_deck))
        for card in dealers_hand:
            if card in current_game_deck:
                current_game_deck.remove(card)
        dealer_cards_dealt += 1
        print('printed dealers hands')
        print(dealers_hand)

    # deal the initial cards to the player
    if player_cards_dealt >= 2:
        blackjack()
        deal_cards_to_player()
        #print(f'{hand_value(players_hand)} - {players_hand}')
    else:
        players_hand.append(random.choice(current_game_deck))
        for card in players_hand:
            if card in current_game_deck:
                current_game_deck.remove(card)
        player_cards_dealt += 1

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

def blackjack(): # CONVERT THIS INTO A BLACKJACK DETECTOR
    global players_hand, dealers_hand, running, game_state
        # Deals a card to player and removes it from the deck.
    if hand_value(dealers_hand) == 21 and hand_value(players_hand) == 21:
        print (f'TIE')
    elif hand_value(dealers_hand) == 21:
        print (f'Dealer Wins!')
    elif hand_value(players_hand) == 21:
        print(f'Blackjack! Player wins!')
        game_state = 'blackjack'
    elif hand_value(players_hand) > 21:
        print(f'Busted with {hand_value(players_hand)-21} Over!\n{players_hand}')
    return 