import requests
import string
import os


def menu():
	pass

def create_word_key(word) -> dict:
	letter_key: dict = {}
	for letter in string.ascii_lowercase:
		letter_key[letter] = 0

	for letter in word:
		letter_key[letter] = word.count(letter)

	return letter_key


def print_all_guesses(current_guess, guess, word) -> None:
	if len(guess) == len(word):
		all_guesses.append(f'{current_guess} - {guess}')
		for value in all_guesses:
			print(value)
	else:
		os.system('cls')
		print('Incorrect Length\n')
		for value in all_guesses:
			print(value)


def correctly_placed(word, guess) -> list[str]:
	current_guess: list[str] = []
	word_key: dict = create_word_key(word)
	
	letter_number: int = 0

	for letter in guess:
		current_guess.append('-')

	for letter in guess:
		# The below is used to initialize a letter
		if letter == word[letter_number] and word_key[letter] > 0:
			current_guess[letter_number] = '+'
			word_key[letter] -= 1
		letter_number += 1
	
	letter_number: int = 0
	for letter in guess:
		if letter in word and word_key[letter] > 0 and current_guess[letter_number] != '+':
			current_guess[letter_number] = '~'
			word_key[letter] -= 1
		letter_number += 1
	return current_guess


def continue_game() -> None:
	global new_word, word, guess_attempt, all_guesses
	continue_input: str = input('\nWould you like to continue? ').lower()
	match continue_input:
		case 'yes':
			new_word = True
			all_guesses = []
			guess_attempt = 0
			word = get_word()
		case _:
			exit()


def get_word() -> str:
	os.system('cls')
	while (True):
		word_length: int = input('How many letters do you want your word to have? ')
		if word_length in string.digits and word_length != '':
			break
		else:
			print('Must be a number!', end = ' ')
	word: str = requests.get(f'https://random-word-api.herokuapp.com/word?length={word_length}').json()[0]
	return word

all_guesses: list[str] = []
new_word: bool = True
word: str = get_word()	

def play() -> None:
	global new_word, word
	guess_attempt: int = 0
	
	while (True):
		os.system('cls')
		print(f'Welcome, you get 5 tries!\n')
		if new_word == True:
			for i in word:
				print('[]', end=' ')
			print()
		else:
			print_all_guesses(current_guess, guess, word)

		guess = input('\nCorrect: + | Incorrect: - | Wrong Spot: ~'
				'\nPlease guess a word: ').lower()

		if len(guess) == len(word):
			new_word = False
			if guess == word:
				os.system('cls')
				print('\nYou Win!')
				continue_game()
			elif guess_attempt > 4:
				os.system('cls')
				print(f'\nYou Lose! The word was: {word}')
				continue_game()
			else:
				current_guess = correctly_placed(word, guess) # was compare_guess()
			guess_attempt += 1



if __name__ == '__main__':
	play()
