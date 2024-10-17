from random import shuffle
from os import system


class GameState:
    # This class will be used to manage the gamestate.  Unsure of what to'
    def __init__(self) -> None:
        self.pot = 0
        self.deck = []
        self.dealers_hand = []
        self.players = {}
        self.has_natural = []
        self.current_turn = 1


game = GameState()


class Player:
    def __init__(self, name) -> None:
        '''Variables: name, hand, chips, dealer'''
        self.name = name
        self.hand = []
        self.chips = 500
        self.dealer = False # pending addition
        self.busted = False
        self.has_natural = False
        self.has_stood = False
        
    
    def __str__(self) -> str:
        return self.name
    
    
    def __repr__(self) -> str:
        return f'Name: {self.name}\nHand: {self.hand}\nChips: {self.chips}'


def create_players():     # for p in players: print(players[p].name)
    while (True):
        try:
            player_num_input = int(input('How many players? '))
            if 7 < player_num_input or 0 >= player_num_input: 
                raise ValueError
            game.players = dict([(f'player_{i+1}', Player(input(f'Player Name: '))) for i in range(player_num_input)])
            break
        except ValueError:
            print('Must be a number! Must be less than 8!', end=' ')
        except TypeError:
            print('Must be a number! Must be less than 8!', end=' ')
    default_deck()


def default_deck():
    while(True):
        input_defaults: str = input('Would you like to use the default deck size(s)? ').lower()
        match input_defaults:
            case 'yes':
                input_deck(True)
                break
            case 'no':
                input_deck(False)
                break
            case _:
                print('Must be yes or no!')


def input_deck(default: bool) -> None:
    if default is True:
        # Determines the number of decks based on the number of players.
        if 1 <= len(game.players) < 3: 
            num_of_decks: int = 2
        elif 3 <= len(game.players) < 5: 
            num_of_decks: int = 4
        elif 5 <= len(game.players) < 7: 
            num_of_decks: int = 6
        else: 
            num_of_decks: int = 8
    else: 
        while(True):
            # Asks the player for the number of decks
            try:
                num_of_decks: int = int(input('How many decks would you like in play? '))
                if not(0 < num_of_decks < 8): 
                    raise ValueError
                break
            except ValueError:
                print('Please pick a number, it must be between 1-8.')
    create_deck(num_of_decks)


def create_deck(num_of_decks: int):
    ten_value_cards = ['J','Q','K']
    suits = ['H','C','D','S']
    while num_of_decks > 0:
        for suit in suits:
                game.deck.append(f'{suit}-A')
                [game.deck.append(f'{suit}-{str(i+2)}') for i in range(9)]
                [game.deck.append(f'{suit}-{card}') for card in ten_value_cards]
        num_of_decks -= 1
    print(f'# of deck: {int(len(game.deck)/52)}')
    shuffle(game.deck)


def deal_card(is_player: bool):
    if is_player == True:
        for p in range(len(game.players)):
            game.players[f'player_{p+1}'].hand.append(game.deck.pop())
    else:
        game.dealers_hand.append(game.deck.pop())


def check_naturals():
    ...


def resolve_naturals():
    ...


def strip_hand(hand: list) -> list:
    stripped_hand = []
    for c in hand:
        discarded_suit, value = c.split('-')
        stripped_hand.append(value)
    return stripped_hand


def card_value(card: str) -> int:
    if card in ['J','Q','K']:
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)


def calc_hand(stripped_hand: list):
    sum_of_cards = 0
    num_of_aces = 0
        # Checks to see the value of a card and totals it (unless it is an ace)
    for card in stripped_hand:
        if card == 'A':
            num_of_aces += 1
        else:
            sum_of_cards = sum_of_cards + card_value(card)
    # Calculates if the total with aces is more than 21, 
    if sum_of_cards + num_of_aces + 10 <= 21 and num_of_aces > 0:
        return sum_of_cards + num_of_aces + 10
    else:
        return sum_of_cards + num_of_aces



def dealers_turn():
    ...


def players_turn(player_key):
    ...


def print_hands():
    ...


def main():
    

    while (True):
        create_players()
        deal_card(is_player=False)
        deal_card(is_player=True)
        deal_card(is_player=False)
        deal_card(is_player=True)
        check_naturals()
        print(f'dealer\'s hand: {game.dealers_hand}')
        [print(f'{game.players[p]}\'s hand: {game.players[p].hand}') for p in game.players]
        break


if __name__ == '__main__':
    main()
