import string

dict_test = {}
word = 'aaabbc'
guess ='acbbbc'
word_key = dict([(letter, word.count(letter)) for letter in word])
print(word_key)
current_guess: list[str] = ['-' for _ in word]
	

def correctly_placed(word, guess) -> list[str]:
	word_key: dict = dict([(letter, word.count(letter)) for letter in string.ascii_lowercase])
	init_guess: list[str] = ['-' for letter in word]
	mid_guess: list[str] = []
	print(word_key)
	print(init_guess)
	print(mid_guess)



def main():
    list = [1,2,3,4,5,6]
    list2 = [i for i in list if i % 2 == 0]
    print(list)
    print(list2)

if __name__ != '__main__':
    main()