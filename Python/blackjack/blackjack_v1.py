import random
import os

def create_deck() -> list:
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
    # Checks to see the value of a card and totals it (unless it is an ace)
    for card in clean_hand:
        if card == 'A':
            number_of_aces += 1
        else:
            normal_card_sum = normal_card_sum + card_value(card)

    # Calculates if the total with aces is more than 21, 
    if normal_card_sum + number_of_aces + 10 <= 21 and number_of_aces > 0:
        return normal_card_sum + number_of_aces + 10
    else:
        return normal_card_sum + number_of_aces

def clear_hand(hand):
    for card in hand:
        print(card)

def continue_game() -> bool:
    ask_to_continue = input('\nWould you like to play another round? ').lower()
    match ask_to_continue:
        case 'yes': 
            return True
        case 'no':
            print('Have a great day!') 
            return False
        case _:
            print('Unknown answer, ending game...')
            return False

def check_outcome(players_hand: list, dealers_hand: list, has_stood: bool) -> bool:
    dealer_score = calculate_hand(dealers_hand)
    player_score = calculate_hand(players_hand)
    if has_stood == False:
        if player_score > 21:
            return False
        else:
            return True
    else:
        if player_score == dealer_score:
            print('It\'s a Tie!')
            return True
        elif player_score > dealer_score or dealer_score > 21:
            print('Player Wins!')
            return True
        else:
            print('House Wins!')
            return True

def players_turn(players_hand, dealers_hand) -> None:
    # Constantly asks if they want to hit, unless they stand.
    while(True):
        # Checks if the player busted, if so break.
        if check_outcome(players_hand, dealers_hand, False) == True:
            # Asks the player for an input, and deals a card on hit, otherwise ends turn.
            player_input = input('Hit or Stand? ').lower()
        else:
            print('You busted! Better luck next time!')
            break
        
        match player_input:
            case 'hit':
                os.system('clear')
                players_hand.append(deal_card(deck))
                print_hands(players_hand, dealers_hand)
                check_outcome(players_hand, dealers_hand, False)
            case 'stand':
                dealers_turn(players_hand, dealers_hand)
                break
            case _:
                print('Invalid Command!')

def dealers_turn(players_hand, dealers_hand):
    if calculate_hand(dealers_hand) < 17:
        while calculate_hand(dealers_hand) < 17:
            os.system('clear')
            dealers_hand.append(deal_card(deck))
            print_hands(players_hand, dealers_hand)
            check_outcome(players_hand, dealers_hand, True)
    else:
        check_outcome(players_hand, dealers_hand, True)

def deal_card(deck):
    return deck.pop()

def print_hands(players_hand, dealers_hand) -> None:
    print(f'The Dealers First Card is always hidden!\n\nDealer: {dealers_hand[1:]} - Score: {calculate_hand(dealers_hand[1:])}')    
    print(f'Player: {players_hand} - Score: {calculate_hand(players_hand)}\n')

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
    while (True):
        os.system('clear')
        global deck
        players_hand = []
        dealers_hand = []

        if len(deck) < 10:
            deck = create_deck()

        # Deal the initial hand to each person.
        dealers_hand.append(deck.pop())
        players_hand.append(deck.pop())
        dealers_hand.append(deck.pop())
        players_hand.append(deck.pop())
        
        print_hands(players_hand, dealers_hand)
        
        if not resolve_naturals(players_hand, dealers_hand):
            players_turn(players_hand, dealers_hand)
            continue_game()
        else:
            continue_game()



        #print('fail')

play()