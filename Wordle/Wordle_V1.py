import requests, os

def menu():
    pass

def count_letters(word):
    letter_key={}
    for letter in word:
        if letter not in letter_key:
            letter_key[letter] = word.count(letter)
    return letter_key


# the below function finds if a letter is in the appropriate place.
def correctly_placed(guess, word):
    letter_number = 0
    previous_guess = []
    word_key = count_letters(word)
    for letter in guess:
        # The below is used to initialize a letter
        previous_guess.append('-')
        # if the letter in position x match the letter in guess and 
        # the key for x > 0 it will replace the '.' value with a '+' confirming its correct.
        if word[letter_number] == letter and word_key[letter] > 0:
            previous_guess[letter_number] = '+'
            word_key[letter] -= 1
        letter_number += 1
    letter_in_word(guess, word, word_key, previous_guess)
    return word_key

def letter_in_word(guess, word, word_key, previous_guess):
    letter_number = 0
    for letter in guess:
        # if the letter in position x match the letter in guess and 
        # the key for x > 0 it will replace the '.' value with a '+' confirming its correct.
        if letter in word and word_key[letter] > 0 and previous_guess[letter_number] != '+':
            previous_guess[letter_number] = '~'
            word_key[letter] -= 1
        letter_number += 1
    print(f'{previous_guess}\n{word_key}')
    return word_key


# previous_guess[5] = 'SUCCESS' - This allows me to replace 

def compare_guess(word, guess):
    letter_number = 0
    previous_guess = []
    word_key = count_letters(word)
    guess_key = count_letters(guess)
    print(word_key)
    correctly_placed(guess, word)
    for letter in guess:
        if letter == word[letter_number]:
            letter_number += 1
            word_key[letter] -= 1
            previous_guess.append('+')
        elif letter in word and word_key[letter] > 1:
            letter_number += 1
            word_key[letter] -= 1
            previous_guess.append('~')
        else:
            letter_number += 1
            previous_guess.append('-')
    return previous_guess

'''
This one is a bit tricky to figure out for above, while it does return + for correct values and 
- for letters not in the word, the ~ will append if the letter exists at all even if no other repeats occur.

'''

def play():
    word = requests.get('https://random-word-api.herokuapp.com/word').json()[0] # stopped working? https://random-word-api.herokuapp.com/word
    word_length = len(word)

    while(True):
        os.system('cls')
        print(word)
        for i in word:
            print('[ ]',end=' ') 

        guess = input('\n\nPlease guess a word: ')
        if len(guess) == len(word):
            compare_guess(word, guess)
            
            # previous_guess.append(guess)
            # print(previous_guess)
            # for word_letter in word:
            #     for guess_letter in guess:
            #         if word_letter == guess_letter:


        

        break


play()

'''
1. Generate the word in the get_letters() 
2. Print the board with six rows of guesses.
3.
4.
5.
'''