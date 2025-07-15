from random import shuffle
from os import system


class GameState:
    # This class will be used to manage the gamestate.
    def __init__(self) -> None:
        self.pot = 0
        self.deck = []
        self.players = {}
        self.has_natural = []
        self.has_stood = []
    
    @classmethod
    def reset_game(self):
        self.pot = 0
        self.deck = []
        self.players = {}
        self.has_natural = []
        self.has_stood = []

        
game = GameState()


class Player:
    def __init__(self, name, dealer = False) -> None:
        '''Variables: name, hand, chips, dealer'''
        self.name = name
        self.hand = []
        self.chips = 500
        self.dealer = dealer
        self.busted = False

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f'\nName: {self.name}\nHand: {self.hand}\nChips: {self.chips}\nDealer: {self.dealer}\nBusted: {self.busted}\nHas Stood: {self.has_stood}'


def create_players():
    while (True):
        try:
            player_num_input = int(input('How many players? '))
            if 7 < player_num_input or 0 >= player_num_input: 
                raise ValueError
            game.players.update([(f'player_{i+1}', Player(input(f'Player Name: '))) for i in range(player_num_input)])
            break
        except ValueError:
            print('Must be a number! Must be less than 8!', end=' ')
        except TypeError:
            print('Must be a number! Must be less than 8!', end=' ')


def create_dealer():
    game.players['player_0'] = Player('dealer', True)


def default_deck():
    while(True):
        input_defaults: str = input('\nWould you like to use the default deck size(s)? ').lower()
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


def deal_card(player_key: str) -> None:
    game.players[f'{player_key}'].hand.append(game.deck.pop())


def check_naturals(hand) -> bool:
    # Checks after the initial deal to see if any cards are natural
    hand = strip_hand(hand)
    if card_value(hand[0]) + card_value(hand[1]) == 21:
        return True
    else:
        return False
    

def resolve_naturals() -> None:
    # Checks which, if any hand have a natural.
    [game.has_natural.append(game.players[p].name) for p in game.players if check_naturals(game.players[p].hand) is True]


def check_natural_wins() -> None:
    '''If the dealer has a natural, they immediately collect the bets of all players who do not have naturals, 
    (but no additional amount). If the dealer and another player both have naturals, the bet of that player is
    a stand-off (a tie), and the player takes back his chips.'''
    
    # Checks the list of naturals
    if 'dealer' in game.has_natural and len(game.has_natural) == 1:
        # if the dealer is the only one with a natural, all players lost their bet. I will need to code bet logic once the game is complete.
        ...
    else:
        [print(f'{item}\'s won!') for item in game.has_natural]
        game.has_natural = []


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


def calc_hand(stripped_hand: list) -> int:
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


def check_hand(hand_value: int) -> None: # May not need this function.
    ...


def dealers_turn() -> None:
    for player in game.players:
        if game.players[player].dealer is True:
            while (True):
                if calc_hand(strip_hand(game.players[player].hand)) < 17:
                    system('cls')
                    deal_card(player)
                    print_hands()
                    print(game.players[player].hand)
                else:
                    break


def players_turn() -> None:
    for player_key in game.players:
        if game.players[player_key].dealer is False and game.players[player_key].name not in game.has_stood:
            print_current_hand(player_key)
            while(True):
                match input('\nHit or Stand? ').lower():
                    case 'hit':
                        deal_card(player_key)
                        print_current_hand(player_key)
                        if len(game.players) > 2:
                            input('\nPress Enter to continue...')
                        break
                    case 'stand':
                        print('stand')
                        game.has_stood.append(game.players[player_key])
                        break
                    case _:
                        print_current_hand(player_key)
                        print(f'\nPlease type "Hit or Stand"')


def print_current_hand(player_key: str) -> None:
    system('cls')
    for item in game.players:
        if game.players[item].dealer == True:
            dealer = item
    p_score = calc_hand(strip_hand(game.players[player_key].hand))
    d_score = calc_hand(strip_hand(game.players[dealer].hand[1:]))
    print(f'Dealer\'s Hand [First Card Hidden]: {game.players[dealer].hand[1:]} - Score: {d_score}')
    print(f'{game.players[player_key].name}\'s Hand [All Cards]: {game.players[player_key].hand} - Score: {p_score}')


def print_hands():
    print(f'dealer\'s hand: {game.players['player_0'].hand[1:]}')
    [print(f'{game.players[p]}\'s hand: {game.players[p].hand}') for p in game.players if game.players[p].dealer is False]


def main():
    while (True):
        # resets the game in full.
        game.reset_game()
        # initializes the dealer as a instance of the player class.
        create_dealer()
        # initializes x number of players and dealer as an instance of the player class.
        create_players()
        # asks the player(s) if they would like to use default values based on the # of players.
        default_deck()

        # deals the initial cards
        [game.players[f'player_{p}'].hand.append(game.deck.pop()) for p in range(len(game.players))]
        [game.players[f'player_{p}'].hand.append(game.deck.pop()) for p in range(len(game.players))]
        system('cls')

        resolve_naturals()

        if len(game.has_natural) > 0:
            check_natural_wins()
            break
        
        # goes through each players turn until they bust or stand.
        while len(game.has_stood) < len(game.players) - 1:
            players_turn()

        dealers_turn()
    
    input('Press enter to continue...')


if __name__ == '__main__':
    main()
