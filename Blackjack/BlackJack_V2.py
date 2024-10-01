from random import shuffle
from os import system

players = {}
deck = []

class Player:
    def __init__(self, name) -> None:
        '''Variables: name, hand, chips, dealer'''
        self.name = name
        self.hand = []
        self.chips = 500
        self.dealer = False

    def __str__(self) -> str:
        return f'Name: {self.name}\nHand: {self.hand}\nChips: {self.chips}'
    
    def __repr__(self) -> str:
        return self.name


def create_players():     # for p in players: print(players[p].name)
    global players
    while (True):
        try:
            player_num_input = int(input('How many players? '))
            if 7 < player_num_input <= 0: 
                raise ValueError
            players = dict([(f'player_{i+1}', i) for i in range(player_num_input)])
            print(players)
            break
        except ValueError:
            print('Must be a number! Must be less than 8!', end=' ')
        except TypeError:
            print('Must be a number! Must be less than 8!', end=' ')

    for entries in players: players[entries] = Player(input(f'Player Name: '))
    default_deck()


def default_deck():
    while(True):
        input_defaults: str = input('Would you like to use the default deck size? ').lower()
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
    global players
    if default is True:
        # Determines the number of decks based on the number of players.
        if 1 <= len(players) < 3: 
            num_of_decks: int = 2
        elif 3 <= len(players) < 5: 
            num_of_decks: int = 4
        elif 5 <= len(players) < 7: 
            num_of_decks: int = 6
        else: 
            num_of_decks: int = 8
    else: 
        while(True):
            # Asks the player for the number of decks
            try:
                deck_input: int = int(input('How many decks would you like in play? '))
                if not(0 < deck_input < 8): 
                    raise ValueError
                num_of_decks: int = deck_input
                break
            except ValueError:
                print('Please pick a number, it must be between 1-8.')
    create_deck(num_of_decks)


def create_deck(num_of_decks: int):
    global deck
    deck = []
    ten_value_cards = ['J','Q','K']
    suits = ['H','C','D','S']
    while num_of_decks > 0:
        for suit in suits:
                deck.append(f'{suit}-{'A'}')
                [deck.append(f'{suit}-{str(i+2)}') for i in range(9)]
                [deck.append(f'{suit}-{card}') for card in ten_value_cards]
        num_of_decks -= 1
    print(f'# of deck: {int(len(deck)/52)}')
    shuffle(deck)



if __name__ == '__main__':
    create_players()