import requests
import os


def create_word_key(word) -> dict:
	letter_key = dict([(letter, word.count(letter)) for letter in word]) 
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
	word_key: dict = create_word_key(word)
	letter_number: int = 0
	init_guess: list[str] = ['-' for letter in word]

	for letter in guess:
		# The below is used to initialize a letter
		if letter == word[letter_number] and word_key.get(letter, 0) > 0:
			init_guess[letter_number] = '+'
			word_key[letter] -= 1
		letter_number += 1

	letter_number: int = 0
	for letter in guess:
		if letter in word and word_key.get(letter, 0) > 0 and init_guess[letter_number] != '+':
			init_guess[letter_number] = '~'
			word_key[letter] -= 1
		letter_number += 1
	return init_guess


def get_word() -> str:
	os.system('cls')
	while (True):
		try:
			word_length: int = input('How many letters do you want your word to have? ')
			word: str = requests.get(f'https://random-word-api.herokuapp.com/word?length={word_length}').json()[0]
			return word
		except ValueError:
			print('Must be a number!', end = ' ')
		except IndexError:
			print('The word length cannot be less than 2 or greater than 15!')
		except ConnectionError | TimeoutError:
			print('Unable to connect to https://random-word-api.herokuapp.com/word')
			exit()


def max_guesses() -> int:
	while (True):
		max_attempts = 5
		try:
			max_attempts: int = int(input('How many guesses would you like? (Default: 5) '))
			if max_attempts < 1: raise ValueError
			return max_attempts
		except ValueError:
			print('Must be a number greater than 0!', end = ' ')


all_guesses: list[str] = []
new_word: bool = True
word: str = get_word()
max_attempts = max_guesses()


def continue_game() -> None:
	global new_word, word, all_guesses, max_attempts
	continue_input: str = input('\nWould you like to continue? ').lower()
	match continue_input:
		case 'yes':
			new_word = True
			all_guesses = []
			word = get_word()
			max_attempts = max_guesses()
			os.system('cls')
		case 'no':
			exit()
		case _:
			print('Please enter yes or no.')


def main() -> None:
	global new_word, word, max_attempts
	guess_attempt: int = 0
	
	while (True):
		# Checks to see if the player has reached the max attempt.
		if guess_attempt == max_attempts:
			print(f'\nYou Lose! The word was: {word}')
			guess_attempt: int = 0
			continue_game()
		# Shows the max attempts and word length.
		os.system('cls')
		print(f'Welcome, you have {max_attempts-guess_attempt} tries!\n')
		if new_word == True:
			for i in word:
				print('[]', end=' ')
			print()
		else:
			print_all_guesses(current_guess, guess, word)
		# Prompts the user for a word/guess.
		guess = input('\nCorrect: + | Incorrect: - | Wrong Spot: ~'
				'\nPlease guess a word: ').lower()
		# Checks to make sure the guess and word are the same length.
		if len(guess) == len(word):
			new_word = False
			guess_attempt += 1
			if guess == word:
				print('\nYou Win!')
				guess_attempt: int = 0
				continue_game()
			else:
				current_guess = correctly_placed(word, guess)


if __name__ == '__main__':
	main()
