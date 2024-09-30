import random

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

players: dict = {}

def create_players():     # for p in players: print(players[p].name)
    global players
    while (True):
        try:
            player_num_input = int(input('How many players? '))
            if 7 < player_num_input <= 0: raise ValueError
            players: dict = dict([(f'player_{i+1}', i) for i in range(player_num_input)])
            print(players)
            break
        except ValueError:
            print('Must be a number! Must be less than 8!', end=' ')
        except TypeError:
            print('Must be a number! Must be less than 8!', end=' ')

    for entries in players:
        players[entries] = Player(input(f'Player Name: '))

def set_dealer():
    # add logic that rotates the dealer after a full round. [Low Priority]
    ...


def create_deck_input(default: bool) -> None:
    if default is True:
        # add logic that determines the number of decks, possibly using match, and then based on the number of players pass the number of decks to create_deck().
        ...
    else:
        # add logic that prompts the player for an input, if that input is within the range 1:8, pass it to create_deck():
        ...


def create_deck(num_of_decks: int) -> list:
    ten_value_cards = ['J','Q','K']
    suits = ['H','C','D','S']
    deck = []

    while (True):
        if num_of_decks == 0: break
        try:
            if not(8 >= int(num_of_decks) > 0): raise ValueError
            for suit in suits:
                deck.append(f'{suit}-{'A'}')
                [deck.append(f'{suit}-{str(i+2)}') for i in range(9)]
                [deck.append(f'{suit}-{card}') for card in ten_value_cards]
            num_of_decks -= 1
        except ValueError:
            print('It must be a number, or if it already is must be less than 8.\nSetting default at 2')
            num_of_decks: int = 2
            
    random.shuffle(deck)
    return deck
    



create_deck(-1)
