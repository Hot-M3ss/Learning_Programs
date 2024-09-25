import requests, os

def menu() -> None:
    os.system('cls')
    print('Welcome to Random Wordle!\n')
    start_game = input('Would you like to play? ').lower()
    match start_game:
        case 'yes':
            play()
        case 'no':
            exit()
        case _:
            print('failed')

def get_letters() -> list:
    print('\nGetting word...')
    response = requests.get('https://random-word-api.herokuapp.com/word',).json()[0]
    return response
    
def guess_word(guess, letters):
    os.system('cls')
    print(f'There are {len(letters)} letters.\n')

    print('Same length!')
    pass

def play() -> None:
    letters = get_letters()
    while(True):
        os.system('cls')
        print(f'There are {len(letters)} letters.\n')
        for letter in letters:
            print('[ ]', end='')

        guess = input('\n\nPlace your guess: ')
        if len(guess) == len(letters):
            guess_word(guess, letters)
            break


play()

