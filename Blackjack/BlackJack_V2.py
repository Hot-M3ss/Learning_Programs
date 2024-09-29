class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.hand = []
        self.chips = 500
        self.dealer = False

    def __str__(self) -> str:
        return f'Name: {self.name}\nHand: {self.hand}\nChips: {self.chips}'
    
    def __repr__(self) -> str:
        return self.name

tim = Player('Tim')


def create_players():
    while (True):
        try:
            player_num_input = int(input('How many players? '))
            if player_num_input < 8:
                players: dict = dict([(f'player_{i+1}', i) for i in range(player_num_input)])
                print(players)
                break
            else:
                print('Players are limited to 7 total.')
        except ValueError:
            print('Must be a number!', end=' ')
        except TypeError:
            print('Must be a number!', end=' ')

    for entries in players:
        players[entries] = Player(input(f'Player Name: '))

    # for p in players:
    #     print(players[p].name)

create_players()
