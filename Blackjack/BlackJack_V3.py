from os import system
from random import shuffle

# Useless class atm.
class Session:
    def __init__(self) -> None:
        pass


class Player:
    def __init__(self, name, dealer = False) -> None:
        self.name = name
        self.hand = []
        self.chips = 500
        self.dealer = dealer

    def __str__(self):
        return self.name


class Table:
    def __init__(self) -> None:
        self.pot = 0
        self.deck = []
        self.players = {}
        self.has_stood = []
        self.has_natural = []


game = Table()


def create_deck() -> list:
    ten_value_cards = ['J','Q','K']
    suits = ['H','C','D','S']
    num_of_decks = 1
    while num_of_decks > 0:
        for suit in suits:
                game.deck.append(f'{suit}-A')
                [game.deck.append(f'{suit}-{str(i+2)}') for i in range(9)]
                [game.deck.append(f'{suit}-{card}') for card in ten_value_cards]
        num_of_decks -= 1
    shuffle(game.deck)


def create_table() -> None:
    game.players['player_0'] = Player('dealer', True)

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


def deal_card(player_id: str) -> None:
    game.players[player_id].hand.append(game.deck.pop())


def print_hands(player_id: str) -> None:
    player = game.players
    system('cls')
    print(f'Dealer\'s Hand [First Card Hidden]: {player['player_0'].hand[1:]} - Score: {calculate_hand(strip_hand(player['player_0'].hand[1:]))}')
    print(f'{player[player_id].name}\'s Hand [All Cards Shown]: {player[player_id].hand} - Score: {calculate_hand(strip_hand(player[player_id].hand))}')


def strip_hand(hand: list) -> list:
    stripped_hand = []

    for card in hand:
        discarded_suit, value = card.split('-')
        stripped_hand.append(value)

    return stripped_hand


def card_value(card: str) -> int:
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)


def calculate_hand(stripped_hand: list) -> None:
    number_of_aces = 0
    sum_of_cards = 0

    for card in stripped_hand:
        if card == 'A': 
            number_of_aces += 1
        else:
            sum_of_cards = sum_of_cards + card_value(card)

    # Calculates if the total with aces is more than 21, 
    if sum_of_cards + number_of_aces + 10 <= 21 and number_of_aces > 0:
        return sum_of_cards + number_of_aces + 10
    else:
        return sum_of_cards + number_of_aces


def check_naturals() -> None:
    # calculates if a natural exists.
    for player_id in game.players:
        if calculate_hand(strip_hand(game.players[player_id].hand)) == 21:
            game.has_natural.append(player_id)
    # if so, compares all people with naturals.
    if len(game.has_natural) > 0:
        resolve_naturals()


def resolve_naturals():
    if game.players['player_0'] in game.has_natural and len(game.has_natural) == 1:
        print('All Bets Lost.')
    elif game.players['player_0'] in game.has_natural and len(game.has_natural) > 1:
        print('Stand off bets returned, non-natural bets lost.')
    else:
        print('All Naturals Payout.')


def players_turn() -> None:
    for player_id in game.players:
        if player_id not in game.has_stood and game.players[player_id].dealer is False:
            print_hands(player_id)
            while(True):
                match input('\nHit or Stand? ').lower():
                    case 'hit':
                        deal_card(player_id)
                        print_hands(player_id)
                        if len(game.players) > 2:
                            input('\nPress Enter to continue...')
                        break
                    case 'stand':
                        game.has_stood.append(player_id)
                        break
                    case _:
                        # print_current_hand(player_key)
                        print(f'\nPlease type "Hit or Stand"')


def dealers_turn():
    if calculate_hand(strip_hand(game.players['player_0'].hand)) < 17:
        deal_card('player_0')
        print(f'\nDealer\'s Hand: {game.players['player_0'].hand}')
    else:
        print(f'\nDealer\'s Hand: {game.players['player_0'].hand}')

def main() -> None:
    while(True):
        # generates the deck
        create_deck()
        # generates the table including dealer/players
        create_table()
        # add bet logic here

        # deal two cards to all players
        [deal_card(player_id) for player_id in game.players]
        [deal_card(player_id) for player_id in game.players]

        # checks for and resolves naturals
        check_naturals()

        if len(game.has_natural) > 0:
            [print(f'{player_id} got paid out!') for player_id in game.has_natural]
            break
        
        # handles the turn order for the game.
        while len(game.has_stood) < len(game.players) - 1:
            players_turn()

        dealers_turn()

        # compare hands & declare a winner
        check_winners()


def check_winners():
    winners = {}
    # Check for and announce winners (pay bets)
    final_hand_values = dict([(player_id, calculate_hand(strip_hand(game.players[player_id].hand))) for player_id in game.players])
    # Returns the highest hand value.
    highest_hand_value = max(final_hand_values.values())
    # reconfigure this to prevent "pushes" from being paid out when a dealer/player tie.
    [print(f'Winner! {game.players[player_id].name}') for player_id in final_hand_values if final_hand_values[player_id] == highest_hand_value]


if __name__ == '__main__':
    main()