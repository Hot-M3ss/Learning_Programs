players_hand = ['D-9', 'S-3', 'H-6', 'C-2']
dealers_hand = ['S-6', 'D-4']
player_cards_dealt = 4
dealer_cards_dealt = 2
    
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

clear_hands()
print(f'Player {players_hand}')
print(f'{player_cards_dealt}')
print(f'Dealers {dealers_hand}')
print(f'{dealer_cards_dealt}')